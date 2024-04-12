import plotly.express as px
from django.db.models import Count
from django.views.generic import TemplateView

from maps.maps_reference_data import SPECIES
from maps.models import CaptureRecord


class BirdsView(TemplateView):
    template_name = "charts/birds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chart_species_capture_count"] = self.get_chart_species_capture_count()
        context["chart_sex_capture_count"] = self.get_chart_sex_capture_count()
        context["chart_age_capture_count"] = self.get_chart_age_capture_count()
        return context

    def get_chart_species_capture_count(self):
        data = CaptureRecord.objects.values("species_number").annotate(capture_count=Count("species_number"))
        x_values = [SPECIES[d["species_number"]]["alpha_code"] for d in data]
        y_values = [d["capture_count"] for d in data]

        fig = px.bar(
            x=x_values,
            y=y_values,
            title="Species Capture Count",
            labels={
                "x": "Species",
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

    def get_chart_sex_capture_count(self):
        data = CaptureRecord.objects.values("sex").annotate(capture_count=Count("sex"))
        x_values = [d["sex"] for d in data]
        y_values = [d["capture_count"] for d in data]

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

    def get_chart_age_capture_count(self):
        data = CaptureRecord.objects.values("age_annual").annotate(capture_count=Count("age_annual"))
        x_values = [d["age_annual"] for d in data]
        y_values = [d["capture_count"] for d in data]

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
        context["chart_net_capture_count"] = self.get_chart_net_capture_count()
        return context

    def get_chart_net_capture_count(self):
        data = CaptureRecord.objects.values("net").annotate(capture_count=Count("net"))
        x_values = [d["net"] for d in data]
        y_values = [d["capture_count"] for d in data]

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
