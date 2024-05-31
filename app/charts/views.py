import plotly.express as px
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.views.generic import TemplateView
from datetime import timedelta

from django.utils.dateparse import parse_date

from birds.models import AgeAnnual
from maps.models import CaptureRecord
from birds.models import Taxon
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
        context["chart_capture_code_count"] = self.get_chart_capture_code_count(date_range)

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
        if date_range:
            start_date, end_date = date_range
            capture_data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .values("species_number", "alpha_code")
                .annotate(capture_count=Count("species_number"))
                .order_by("-species_number")
            )
        else:
            capture_data = (
                CaptureRecord.objects.values("species_number")
                .values("species_number", "alpha_code")
                .annotate(capture_count=Count("species_number"))
                .order_by("-species_number")
            )

        species_numbers = {item["species_number"] for item in capture_data}
        taxons = Taxon.objects.filter(number__in=species_numbers)
        taxon_map = {taxon.number: taxon.common for taxon in taxons}

        enhanced_data = [
            {
                "common_name": taxon_map.get(item["species_number"]),
                "capture_count": item["capture_count"],
                "alpha_code": item["alpha_code"]
            }
            for item in capture_data
        ]

        x_values = [d["capture_count"] for d in enhanced_data]
        y_values = [d["alpha_code"] for d in enhanced_data]
        y_names = [d["common_name"] for d in enhanced_data]

        if not (x_values):
            return "No data available for the selected date range."

        title_height = 20
        bar_thickness = 30
        chart_height = bar_thickness * len(y_values) + title_height

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=None,
            labels={
                "x": "Capture Count",
                "y": "Species",
            },
            text=x_values,
            orientation="h",
            template="plotly_white",
        )

        fig.update_traces(
            textfont={"weight": "bold"},
            textangle=0,
            textposition="auto",
            customdata=y_names,
            hovertemplate="<br>".join([
                "<b><span style='font-size: 16px;'>%{customdata}</span></b>",  # Apply font size here
                "<extra></extra>"  # Hides the secondary box in the hover tooltip
            ])
        )

        fig.update_layout(
            showlegend=False,
            barmode="relative",
            height=chart_height,
            margin={
                "l": 0,
                "r": 0,
                "t": 0,
                "b": 0,
                "pad": 0,
            },
            xaxis={
                "title": None,
                "fixedrange": True,
            },
            yaxis={
                "title": None,
                "fixedrange": True,
                "side": "left",
                "showticklabels": True,
                "ticklabelposition": "inside",
                "tickfont": {
                    "weight": "bold",
                }
            },
            dragmode=False,
        )

        config = {"displayModeBar": False}

        return fig.to_html(config=config)

    def get_chart_sex_capture_count(self, date_range=None):
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects
                .filter(capture_time__date__range=[start_date, end_date])
                .values("sex")
                .annotate(capture_count=Count("sex"))
            )
        else:
            data = (
                CaptureRecord.objects
                .values("sex")
                .annotate(capture_count=Count("sex"))
            )

        sex_map = {"M": "Male", "F": "Female", "U": "Unkown"}
        labels = [sex_map.get(d["sex"]) for d in data]
        values = [d["capture_count"] for d in data]

        chart_height = 300 

        if not (labels and values):
            return ""

        fig = px.pie(
            names=labels,
            values=values,
            title=None,
            color=labels,
            template="plotly_white",
        )

        fig.update_traces(
            textinfo="percent+label",
            textfont={"weight": "bold"},
            marker={
                "line": {
                    "color": "#333",
                    "width": 1
                }
            },
        )

        fig.update_layout(
            legend={
                "x": 1.05,
                "xanchor": "left",
                "y": 0.5,
                "yanchor": "middle"
            },
            margin={
                "l": 10,
                "r": 0,
                "t": 0,
                "b": 0,
                "pad": 10,
            },
            height=chart_height,
        )

        return fig.to_html(config=self.config)

    def get_chart_age_capture_count(self, date_range=None):
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects
                .filter(capture_time__date__range=[start_date, end_date])
                .values("age_annual")
                .annotate(capture_count=Count("age_annual"))
            )
        else:
            data = (
                CaptureRecord.objects
                .values("age_annual")
                .annotate(capture_count=Count("age_annual"))
            )

        age_codes = {item["age_annual"] for item in data}
        ages = AgeAnnual.objects.filter(number__in=age_codes).values()
        age_map = {age["number"]: (age["alpha"], age["description"], age["explanation"], age["explanation"]) for age in ages}

        enhanced_data = [
            {
                "age_alpha": age_map.get(item["age_annual"])[0], 
                "description": age_map.get(item["age_annual"])[1],
                "explanation": age_map.get(item["age_annual"])[2], 
                "capture_count": item["capture_count"]
            }
            for item in data if item["age_annual"] in age_map
        ]

        # Function to insert line breaks every n characters in a string
        def insert_line_breaks(text, n=50):
            return '<br>'.join(text[i:i+n] for i in range(0, len(text), n))

        labels = [d["description"] for d in enhanced_data]
        values = [d["capture_count"] for d in enhanced_data]
        text_labels = [d["age_alpha"] for d in enhanced_data]
        explanations = [d["explanation"] for d in enhanced_data]
        formatted_explanations = [insert_line_breaks(exp) for exp in explanations]

        legend_height = 20 * len(labels) + 40
        chart_height = 300 + legend_height

        if not (labels and values):
            return ""

        fig = px.pie(
            names=labels,
            values=values,
            title=None,
            template="plotly_white"
        )

        fig.update_traces(
            text=text_labels,
            textinfo="percent+text",
            textfont={"weight": "bold"},
            marker={
                "line": {
                    "color": "#333",
                    "width": 1
                },
            },
            customdata=formatted_explanations,
            hovertemplate=(
                "<b>%{label} (%{value})</b><br>"
                "%{customdata}"
                "<extra></extra>"  # Hides the secondary box in the hover tooltip
            )
        )

        fig.update_layout(
            legend={
                "x": 0,
                "xanchor": "center",
                "y": 1,
                "yanchor": "bottom"
            },
            margin={
                "l": 10,
                "r": 0,
                "t": 0,
                "b": 0,
                "pad": 10,
            },
            height=chart_height,
        )

        config = {"displayModeBar": False}

        return fig.to_html(config=config)

    def get_chart_days_capture_count(self, date_range=None):
        if date_range:
            start_date, end_date = date_range
            data = (
                CaptureRecord.objects.filter(capture_time__date__range=[start_date, end_date])
                .annotate(capture_day=TruncDate("capture_time"))
                .values("capture_day")
                .annotate(capture_count=Count("id"))
                .order_by("-capture_day")
            )
        else:
            data = (
                CaptureRecord.objects.annotate(capture_day=TruncDate("capture_time"))
                .values("capture_day")
                .annotate(capture_count=Count("id"))
                .order_by("-capture_day")
            )

        x_values = [d["capture_count"] for d in data]
        y_values = [d["capture_day"].strftime("%m/%d") for d in data]

        if not (x_values and y_values):
            return ""

        bar_thickness = 40
        chart_height = bar_thickness * len(y_values)

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=None,
            labels={
                "x": "Capture Count",
                "y": "Capture Day",
            },
            text=x_values,
            orientation="h",
            template="plotly_white"
        )

        fig.update_traces(
            textfont={
                "weight": "bold",
            },
            textangle=0,
            textposition="auto",
        )

        fig.update_layout(
            showlegend=False,
            barmode="relative",
            height=chart_height,
            margin={
                "l": 0,
                "r": 0,
                "t": 0,
                "b": 0,
                "pad": 10,
            },
            xaxis={
                "title": None,
                "fixedrange": True,
            },
            yaxis={
                "title": None,
                "side": "left",
                "showticklabels": True,
                "ticklabelposition": "inside",
                "tickfont": {
                    "weight": "bold",
                }
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
        y_values = [f"Net: {d['net']}" for d in data]

        if not (x_values and y_values):
            return ""

        title_height = 20
        bar_thickness = 40
        chart_height = 100 + (bar_thickness * len(y_values)) + title_height

        fig = px.bar(
            x=x_values,
            y=y_values,
            title=figure_title,
            labels={
                "x": "Capture Count",
                "y": "Net",
            },
            text=x_values,
            orientation="h",
            template="plotly_white"
        )

        fig.update_traces(
            textfont={
                "weight": "bold",
            },
            textangle=0,
            textposition="auto",
        )

        fig.update_layout(
            title=None,
            showlegend=False,
            barmode="relative",
            height=chart_height,
            margin={
                "l": 0,
                "r": 0,
                "t": 0,
                "b": 0,
                "pad": 10,
            },
            xaxis={
                "title": None,
                "fixedrange": True,
            },
            yaxis={
                "title": None,
                "side": "left",
                "showticklabels": True,
                "fixedrange": True,
                "ticklabelposition": "inside",
                "tickfont": {
                    "weight": "bold",
                }
            },
            dragmode=False,
        )

        config = {"displayModeBar": False}

        return fig.to_html(config=config)

    def get_chart_capture_code_count(self, date_range=None):
        if date_range:
            start_date, end_date = date_range
            capture_data = (
                CaptureRecord.objects
                .filter(capture_time__date__range=[start_date, end_date])
                .values("capture_code")
                .annotate(capture_count=Count("capture_code"))
            )
        else:
            capture_data = (
                CaptureRecord.objects
                .values("capture_code")
                .annotate(capture_count=Count("capture_code"))
            )

        capture_code_map = {
            "N": "New",
            "R": "Recaptured",
            "L": "Lost",
            "D": "Destroyed Band (and or dead)",
            "U": "Unbanded",
            "C": "Changed",
            "A": "Added",
        }

        labels = [capture_code_map.get(d["capture_code"]) for d in capture_data]
        values = [d["capture_count"] for d in capture_data]

        chart_height = 300

        if not(labels and values):
            return ""
        
        fig = px.pie(
            names=labels,
            values=values,
            title=None,
            color=labels,
            template="plotly_white",
        )

        fig.update_traces(
            textinfo="percent+label",
            textfont={"weight": "bold"},
            marker={
                "line": {
                    "color": "#333",
                    "width": 1
                }
            },
        )

        fig.update_layout(
            legend={
                "x": 0,
                "xanchor": "center",
                "y": 1,
                "yanchor": "bottom"
            },
            margin={
                "l": 10,
                "r": 0,
                "t": 0,
                "b": 0,
                "pad": 10,
            },
            height=chart_height,
        )

        return fig.to_html(config=self.config)