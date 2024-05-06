import plotly.express as px
from django.db.models import Count
from django.views.generic import TemplateView

from maps.maps_reference_data import SPECIES
from maps.models import CaptureRecord


class BirdsView(TemplateView):
    template_name = "charts/birds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.GET.get("date", None)
        context["chart_species_capture_count"] = self.get_chart_species_capture_count(date)
        context["chart_sex_capture_count"] = self.get_chart_sex_capture_count(date)
        context["chart_age_capture_count"] = self.get_chart_age_capture_count(date)
        return context

    # def get_chart_species_capture_count(self, date=None):
    #     if date:
    #         data = CaptureRecord.objects.filter(capture_time__date=date).values("species_number").annotate(capture_count=Count("species_number"))
    #     else:
    #         data = CaptureRecord.objects.values("species_number").annotate(capture_count=Count("species_number"))

    #     x_values = [SPECIES[d["species_number"]]["alpha_code"] for d in data]
    #     y_values = [d["capture_count"] for d in data]

    #     # Get the number of x_values that will be displayed in the chart
    #     x_values_count = len(x_values)

    #     # Get the capture count of the 5th most captured species
    #     bottom_cutoff = sorted(y_values, reverse=True)[4]
    #     print(bottom_cutoff)

    #     if not (x_values and y_values):
    #         return ""
        
    #     colors = ["red" if count >= bottom_cutoff else "blue" for count in y_values]

    #     fig = px.bar(
    #         x=x_values,
    #         y=y_values,
    #         title="Species Capture Count",
    #         labels={
    #             "x": "Species",
    #             "y": "Capture Count",
    #         },
    #         text_auto=True,
    #         color=colors,
    #     )
    #     fig.update_traces(textfont_size=14, textangle=0, textposition="inside")
    #     fig.update_layout(
    #         title={
    #             "font_size": 22,
    #             "xanchor": "center",
    #             "x": 0.5,
    #         },
    #         showlegend=False,
    #     )
    #     return fig.to_html()

    def get_chart_species_capture_count(self, date=None):
        if date:
            data = CaptureRecord.objects.filter(capture_time__date=date).values("species_number").annotate(capture_count=Count("species_number"))
        else:
            data = CaptureRecord.objects.values("species_number").annotate(capture_count=Count("species_number"))

        x_values = [d["capture_count"] for d in data]  # Use capture count as x-values for horizontal bars
        y_values = [SPECIES[d["species_number"]]["alpha_code"] for d in data]

        # Get the number of y_values that will be displayed in the chart
        y_values_count = len(y_values)

        # Get the capture count of the 5th most captured species
        top_five_lower_count = sorted(x_values, reverse=True)[4]
        print(top_five_lower_count)

        if not (x_values and y_values):
            return ""
        
        colors = ["Top 5" if count >= top_five_lower_count else "other" for count in x_values]

        fig = px.bar(
            x=x_values,  # Use capture count as x-values
            y=y_values,  # Use species code as y-values
            title="Species Capture Count",
            labels={
                "x": "Capture Count",  # Update labels accordingly
                "y": "Species",         # Update labels accordingly
            },
            text_auto=True,
            color=colors,
            orientation="h",  # Set orientation to horizontal
        )
        fig.update_traces(textfont_size=20, textangle=0, textposition="inside")
        fig.update_layout(
            title={
                "font_size": 22,
                "xanchor": "center",
                "x": 0.5,
            },
            showlegend=False,
            barmode="relative",
            bargap=0.2,
            height=100 + 25 * y_values_count,
        )

        return fig.to_html()


    def get_chart_sex_capture_count(self, date=None):
        if date:
            data = CaptureRecord.objects.filter(capture_time__date=date).values("sex").annotate(capture_count=Count("sex"))
        else:
            data = CaptureRecord.objects.values("sex").annotate(capture_count=Count("sex"))

        x_values = [d["sex"] for d in data]
        y_values = [d["capture_count"] for d in data]

        if not (x_values and y_values):
            return ""

        fig = px.bar(
            x=x_values,
            y=y_values,
            title="Sex Capture Count",
            labels={
                "x": "Sex",
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

    def get_chart_age_capture_count(self, date=None):
        if date:
            data = CaptureRecord.objects.filter(capture_time__date=date).values("age_annual").annotate(capture_count=Count("age_annual"))
        else:
            data = CaptureRecord.objects.values("age_annual").annotate(capture_count=Count("age_annual"))

        x_values = [d["age_annual"] for d in data]
        y_values = [d["capture_count"] for d in data]

        if not (x_values and y_values):
            return ""

        fig = px.bar(
            x=x_values,
            y=y_values,
            title="Age Capture Count",
            labels={
                "x": "Age",
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
