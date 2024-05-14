import plotly.express as px
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.views.generic import TemplateView
from datetime import timedelta

from django.utils.dateparse import parse_date

from maps.maps_reference_data import SPECIES
from maps.models import CaptureRecord
from .forms import DateForm


class BirdsView(TemplateView):
    template_name = "charts/birds.html"

    color_array = [
        "#ffa600",  # yellow
        "#003f5c",  # navy
        "#ff7c43",  # orange
        "#2f4b7c",  # blue
        "#d45087",  # fuchsia
        "#665191",  # plum
        "#f95d6a",  # melon
        "#a05195",  # purple
    ]

    config = {
        "staticPlot": True,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date_form = DateForm(self.request.GET)
        context["date_form"] = date_form
        date_range = self.get_date_range(self.request)

        context["color_array"] = self.color_array
        context["capture_count_total"] = self.get_total_capture_count(date_range)
        context["capture_days"] = self.get_all_capture_days()
        context["chart_species_capture_count"] = self.get_chart_species_capture_count(date_range)
        context["chart_sex_capture_count"] = self.get_chart_sex_capture_count(date_range)
        context["chart_age_capture_count"] = self.get_chart_age_capture_count(date_range)
        context["chart_days_capture_count"] = self.get_chart_days_capture_count(date_range)
        context["chart_net_capture_count"] = self.get_chart_net_capture_count(date_range)

        return context

    def get_date_range(self, request):
        date_range_str = request.GET.get("date_range")
        if date_range_str:
            dates = date_range_str.split(" to ")
            if len(dates) == 1:
                # Only one date provided, use the same date as start and end
                start_date = parse_date(dates[0])
                if start_date:
                    end_date = start_date + timedelta(days=1)  # Set end_date to the next day for inclusive filtering
                    return (start_date, end_date)
            elif len(dates) == 2:
                # Two dates provided, parse both
                start_date, end_date = (parse_date(date) for date in dates)
                if start_date and end_date:
                    return (start_date, end_date)
        return None

    def get_total_capture_count(self, date_range=None):
        if date_range:
            start_date, end_date = date_range
            capture_count = CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date]).count()
        else:
            capture_count = CaptureRecord.objects.count()

        return capture_count

    # Get all days for which there are capture records in the database
    def get_all_capture_days(self):
        # Truncate datetime to date and retrieve unique dates, formatted as strings
        capture_days = (
            CaptureRecord.objects.annotate(
                capture_day=TruncDate("capture_time"),
            )
            .order_by("capture_day")
            .values_list("capture_day", flat=True)
            .distinct()
        )

        # Format each date as 'YYYY-MM-DD'
        formatted_capture_days = [day.strftime("%Y-%m-%d") for day in capture_days if day]

        return formatted_capture_days

    def get_chart_species_capture_count(self, date_range=None):
        figure_title = "Capture Count by Species"
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .values("species_number")
                .annotate(capture_count=Count("species_number"))
            )
        else:
            data = CaptureRecord.objects.values("species_number").annotate(capture_count=Count("species_number"))

        x_values = [d["capture_count"] for d in data]
        y_values = [SPECIES[d["species_number"]]["alpha_code"] for d in data]

        if not (x_values):
            return "No data available for the selected date range."

        sorted_x_values = sorted(x_values, reverse=True)
        cuttoff_index = max(int(len(sorted_x_values) * 0.25) - 1, 0)
        top_25_percent_lower_count = sorted_x_values[cuttoff_index] if sorted_x_values else 0
        colors = [self.color_array[0] if x >= top_25_percent_lower_count else self.color_array[1] for x in x_values]
        bar_thickness = 30
        chart_height = 100 + bar_thickness * len(y_values)

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": "Capture Count",
                "y": "Species",
            },
            text=[f"{y} ({x})" for x, y in zip(x_values, y_values)],
            orientation="h",
        )

        fig.update_traces(
            marker_color=colors,
            textangle=0,
            textposition="auto",
            textfont={
                "weight": "bold",
            },
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
            margin={
                "l": 0,
                "r": 0,
                "t": 30,
                "b": 0,
                "pad": 10,
            },
            yaxis_title="",
            xaxis_title="",
            yaxis={
                "side": "right",
                "showticklabels": False,
            },
        )

        return fig.to_html(config=self.config)

    def get_chart_sex_capture_count(self, date_range=None):
        figure_title = "Capture Count by Sex"
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .values("sex")
                .annotate(capture_count=Count("sex"))
            )
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
            text_auto=True,
        )

        fig.update_traces(
            textfont={
                "weight": "bold",
            },
            textangle=0,
            textposition="inside",
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
            margin={
                "l": 0,
                "r": 0,
                "t": 30,
                "b": 0,
                "pad": 10,
            },
            yaxis_title="",
            xaxis_title="",
            yaxis={
                "side": "right",
                "ticklabelposition": "inside top",
            },
        )

        return fig.to_html(config=self.config)

    def get_chart_age_capture_count(self, date_range=None):
        figure_title = "Capture Count by Age"
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .values("age_annual")
                .annotate(capture_count=Count("age_annual"))
            )
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
        data = [
            {"age_annual": age_code_map.get(item["age_annual"], "Unknown"), "capture_count": item["capture_count"]}
            for item in data
        ]

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
            textfont={
                "weight": "bold",
            },
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
            margin={
                "l": 0,
                "r": 0,
                "t": 30,
                "b": 0,
                "pad": 10,
            },
            yaxis_title="",
            xaxis_title="",
            yaxis={
                "side": "right",
                "ticklabelposition": "inside top",
            },
        )

        return fig.to_html(config=self.config)

    def get_chart_days_capture_count(self, date_range=None):
        figure_title = "Capture Count by Day"
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .annotate(capture_day=TruncDate("capture_time"))
                .values("capture_day")
                .annotate(capture_count=Count("id"))
                .order_by("capture_day")
            )
        else:
            data = (
                CaptureRecord.objects.annotate(capture_day=TruncDate("capture_time"))
                .values("capture_day")
                .annotate(capture_count=Count("id"))
                .order_by("capture_day")
            )

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
            text=[f"{y} ({x})" for x, y in zip(x_values, y_values)],
            color=y_values,
            color_discrete_map=color_map,
            orientation="h",
        )

        fig.update_traces(
            textfont={
                "weight": "bold",
            },
            textangle=0,
            textposition="inside",
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
            margin={
                "l": 0,
                "r": 0,
                "t": 30,
                "b": 0,
                "pad": 10,
            },
            yaxis_title="",
            xaxis_title="",
            yaxis_tickformat="%m-%d",
            yaxis={
                "side": "right",
                "showticklabels": False,
            },
        )

        return fig.to_html(config=self.config)

    def get_chart_net_capture_count(self, date_range=None):
        figure_title = "Capture Count by Net"
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .values("net")
                .annotate(capture_count=Count("net"))
            )
        else:
            data = CaptureRecord.objects.values("net").annotate(capture_count=Count("net"))

        x_values = [d["capture_count"] for d in data]
        y_values = [str(d["net"]) for d in data]

        if not (x_values and y_values):
            return ""

        bar_thickness = 40
        chart_height = 100 + bar_thickness * len(y_values)

        color_map = {str(net): self.color_array[i % len(self.color_array)] for i, net in enumerate(sorted(y_values))}

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": "Capture Count",
                "y": "Nets",
            },
            text=[f"net:{net} ({count})" for net, count in zip(y_values, x_values)],
            color=y_values,
            color_discrete_map=color_map,
            orientation="h",
        )

        fig.update_traces(
            textfont={
                "weight": "bold",
            },
            textangle=0,
            textposition="auto",
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
            margin={
                "l": 0,
                "r": 0,
                "t": 30,
                "b": 0,
                "pad": 10,
            },
            yaxis_title="",
            xaxis_title="",
            yaxis={
                "side": "right",
                "showticklabels": False,
            },
        )

        return fig.to_html(config=self.config)
