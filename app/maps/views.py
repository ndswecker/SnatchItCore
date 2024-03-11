from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

import maps.maps_reference_data as REFERENCE_DATA
from .forms import CaptureRecordForm
from .models import CaptureRecord
from common.species_summary import SpeciesSummary
from users.mixins import ApprovalRequiredMixin


def get_band_sizes_for_species(request):
    species_number = request.GET.get("species_number")
    band_sizes = REFERENCE_DATA.SPECIES.get(int(species_number), {}).get("band_sizes", [])
    return JsonResponse({"band_sizes": band_sizes})


def get_species(request):
    species_number = request.GET.get("species_number")
    species_info = REFERENCE_DATA.SPECIES.get(int(species_number))  # Convert string to int and get species info

    if species_info:
        species_summary = SpeciesSummary(species_info)
        html_snippet = species_summary.generate_html_snippet()
        return HttpResponse(html_snippet, content_type="text/html")  # Return the HTML snippet in the response
    else:
        # If species info not found, return an error message as HTML or consider using a 404 page
        return HttpResponse("<p>Species not found.</p>", status=404, content_type="text/html")


class CreateCaptureRecordView(LoginRequiredMixin, ApprovalRequiredMixin, CreateView):
    template_name = "maps/enter_bird.html"
    form_class = CaptureRecordForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.bander_initials = self.request.user.initials
        self.object = form.save()
        return redirect(reverse_lazy("maps:detail_capture_record", kwargs={"pk": self.object.pk}))


class DetailCaptureRecordView(LoginRequiredMixin, DetailView):
    template_name = "maps/detail.html"
    model = CaptureRecord
    context_object_name = "capture_record"


class ListCaptureRecordView(LoginRequiredMixin, ListView):
    template_name = "maps/list_all.html"
    model = CaptureRecord
    context_object_name = "capture_records"

    def get_queryset(self):
        return CaptureRecord.objects.filter(user=self.request.user)
