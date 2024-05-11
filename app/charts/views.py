import plotly.express as px
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.views.generic import TemplateView

from django.utils.html import format_html
from django.utils.dateparse import parse_date

from maps.maps_reference_data import SPECIES
from maps.models import CaptureRecord
from .forms import DateForm

class BirdsView(TemplateView):
    template_name = "charts/birds.html"

    color_array = [
        "#ffa600", # yellow
        "#003f5c", # navy
        "#ff7c43", # orange
        "#2f4b7c", # blue
        "d45087", # fuschia
        "#665191", # plum
        "#f95d6a", # melon
        "#a05195", # purple
    ]
    config = {
            "staticPlot": True,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date_form = DateForm(self.request.GET)
        context["date_form"] = date_form
        date_range = None

        start_date_str = self.request.GET.get("start")
        end_date_str = self.request.GET.get("end")

        if start_date_str and end_date_str:
            start_date = parse_date(start_date_str)
            end_date = parse_date(end_date_str)
            date_range = (start_date, end_date)

        context["color_array"] = self.color_array
        context["capture_count_total"] = self.get_total_capture_count(date_range)
        context["chart_species_capture_count"] = self.get_chart_species_capture_count(date_range)
        context["chart_sex_capture_count"] = self.get_chart_sex_capture_count(date_range)
        context["chart_age_capture_count"] = self.get_chart_age_capture_count(date_range)
        context["chart_days_capture_count"] = self.get_chart_days_capture_count(date_range)

        return context


    # Method to get the number of the total capture count for all captures in the current date range
    def get_total_capture_count(self, date_range=None):
        if date_range:
            start_date, end_date = date_range
            capture_count = CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date]).count()
        else:
            capture_count = CaptureRecord.objects.count()
        
        return capture_count

    def get_chart_species_capture_count(self, date_range=None):
        figure_title = "Capture Count by Species"
        if date_range:
            start_date, end_date = date_range
            data = CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date]).values("species_number").annotate(capture_count=Count("species_number"))
        else:
            data = CaptureRecord.objects.values("species_number").annotate(capture_count=Count("species_number"))

        x_values = [d["capture_count"] for d in data]  # Use capture count as x-values for horizontal bars
        y_values = [SPECIES[d["species_number"]]["alpha_code"] for d in data]

        # Get the capture count of the 5th most captured species
        # This will be used to determine if a species is in the top 5 or not
        # More than 5 species might be considered in the top 5 if they have the same capture count as the 5th most captured species
        top_five_lower_count = sorted(x_values, reverse=True)[4]

        if not (x_values and y_values):
            return ""
        
        colors = ["Top 5" if count >= top_five_lower_count else "other" for count in x_values]
        # map the colors to the color_array
        color_map = {value: self.color_array[i] for i, value in enumerate(sorted(set(colors)))}

        bar_thickness = 30
        chart_height = 100 + bar_thickness * len(y_values)

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": f"Capture Count ({sum(x_values)})",
                "y": "Species",
            },
            text=[f"{y} ({x})" for x, y in zip(x_values, y_values)], 
            color=colors,
            color_discrete_map=color_map,
            orientation="h",
        )

        fig.update_traces(
            textangle=0, 
            textposition="auto",
            textfont=dict(weight="bold"),
        )

        fig.update_layout(
            title={
                "font": {
                    "size": 18,
                },
                "xanchor": "left",
                "yanchor": "top",
                "x": 0,
                "y": 1,
                "pad": {"b": 0, "t": 0},
            },
            showlegend=False,
            barmode="relative",
            height=chart_height,
            margin=dict(l=0, r=0, t=30, b=0, pad=10),
            yaxis_title="",
            yaxis=dict(
                side="right",
                showticklabels=False,
            ),
        )

        return fig.to_html(config=self.config)


    def get_chart_sex_capture_count(self, date_range=None):
        figure_title = "Capture Count by Sex"
        if date_range:
            start_date, end_date = date_range
            data = CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date]).values("sex").annotate(capture_count=Count("sex"))
        else:
            data = CaptureRecord.objects.values("sex").annotate(capture_count=Count("sex"))

        x_values = [d["sex"] for d in data]
        y_values = [d["capture_count"] for d in data]

        if not (x_values and y_values):
            return ""
        
        unique_sexes = sorted(set(x_values))
        color_map = {sex: self.color_array[i % len(self.color_array)] for i, sex in enumerate(unique_sexes)}

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": "Sex",
                "y": "Capture Count",
            },
            color=x_values,
            color_discrete_map=color_map,
        )

        fig.update_traces(
            textfont=dict(
                color="white", 
                weight="bold"
            ), 
            textangle=0, 
            textposition="inside"
        )

        fig.update_layout(
            title={
                "font": {
                    "size": 18,
                },
                "xanchor": "left",
                "yanchor": "top",
                "x": 0,
                "y": 1,
                "pad": {"b": 0, "t": 0},
            },
            showlegend=False,
            margin=dict(l=0, r=0, t=30, b=0, pad=10),
            yaxis_title="",
            xaxis_title="",
            yaxis=dict(
                side="right",
                ticklabelposition="inside top",
            ),
        )

        return fig.to_html(config=self.config)

    def get_chart_age_capture_count(self, date_range=None):
        figure_title = "Capture Count by Age"
        if date_range:
            start_date, end_date = date_range
            data = CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date]).values("age_annual").annotate(capture_count=Count("age_annual"))
        else:
            data = CaptureRecord.objects.values("age_annual").annotate(capture_count=Count("age_annual"))

        age_code_map = {
            4: "L",
            2: "HY",
            1: "AHY",
            5: "SY",
            6: "ASY",
            7: "TY",
            8: "ATY",
            0: "U",
            9: "U",
        }
        data = [{"age_annual": age_code_map.get(item["age_annual"], "Unknown"), "capture_count": item["capture_count"]} for item in data]

        x_values = [d["age_annual"] for d in data]
        y_values = [d["capture_count"] for d in data]

        if not (x_values and y_values):
            return ""
        
        unique_ages = sorted(set(x_values))
        color_map = {age: self.color_array[i % len(self.color_array)] for i, age in enumerate(unique_ages)}

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": "Age",
                "y": "Capture Count",
            },
            color=x_values,
            color_discrete_map=color_map,
            text_auto=True,
        )

        fig.update_traces(
            textangle=0, 
            textposition="inside",
            textfont=dict(weight="bold"),
        )

        fig.update_layout(
            title={
                "font": {
                    "size": 18,
                },
                "xanchor": "left",
                "yanchor": "top",
                "x": 0,
                "y": 1,
                "pad": {"b": 0, "t": 0},
            },
            showlegend=False,
            barmode="relative",
            margin=dict(l=0, r=0, t=30, b=0, pad=10),
            yaxis_title="",
            xaxis_title="",
            yaxis=dict(
                side="right",
                ticklabelposition="inside top",
            ),
        )

        return fig.to_html(config=self.config)
    
    def get_chart_days_capture_count(self, date_range=None,):
        figure_title = "Capture Count by Day"
        if date_range:
            start_date, end_date = date_range
            data = CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date]) \
                .annotate(capture_day=TruncDate('capture_time')) \
                .values("capture_day") \
                .annotate(capture_count=Count("id")) \
                .order_by("capture_day")
        else:
            data = CaptureRecord.objects.annotate(capture_day=TruncDate('capture_time')) \
                .values("capture_day") \
                .annotate(capture_count=Count("id")) \
                .order_by("capture_day")

        x_values = [d["capture_count"] for d in data]
        y_values = [d["capture_day"].strftime("%m/%d") for d in data]


        if not (x_values and y_values):
            return ""
        
        # For each day, set the color map to the color_array
        color_map = {day: self.color_array[i % len(self.color_array)] for i, day in enumerate(sorted(set(y_values)))}
        
        bar_thickness = 40
        chart_height = 100 + bar_thickness * len(y_values)

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": "Capture Count",
                "y": "Capture Day",
            },
            # text_auto=True,
            text=[f"{y} ({x})" for x, y in zip(x_values, y_values)],
            color=y_values,
            color_discrete_map=color_map,
            orientation="h",
        )

        fig.update_traces(
            textfont=dict(
                weight="bold",
            ),
            textangle=0, 
            textposition="inside"
        )

        fig.update_layout(
            title={
                "font": {
                    "size": 18,
                },
                "xanchor": "left",
                "yanchor": "top",
                "x": 0,
                "y": 1,
                "pad": {"b": 0, "t": 0},
            },
            showlegend=False,
            barmode="relative",
            bargap=0.2,
            height=chart_height,
            margin=dict(l=0, r=0, t=30, b=0, pad=10),
            yaxis_title="",
            xaxis_title="",
            yaxis_tickformat='%m-%d',
            yaxis=dict(
                side="right",
                showticklabels=False,
            ),
        )

        return fig.to_html(config=self.config)
        

class NetsView(TemplateView):
    template_name = "charts/nets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.GET.get("date", None)
        context["chart_net_capture_count"] = self.get_chart_net_capture_count(date)
        return context

    def get_chart_net_capture_count(self, date=None):
        if date:
            data = CaptureRecord.objects.filter(capture_time__date=date).values("net").annotate(capture_count=Count("net"))
        else:
            data = CaptureRecord.objects.values("net").annotate(capture_count=Count("net"))

        x_values = [d["net"] for d in data]
        y_values = [d["capture_count"] for d in data]

        if not (x_values and y_values):
            return ""

        fig = px.bar(
            x=x_values,
            y=y_values,
            title="Net Capture Count",
            labels={
                "x": "Net",
                "y": "Capture Count",
            },
            text_auto=True,
        )
        fig.update_traces(textfont_size=14, textangle=0, textposition="inside")
        fig.update_layout(
            title={
                "font_size": 22,
                "xanchor": "center",
                "x": 0.5,
            },
        )
        return fig.to_html()
