from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.utils import timezone

import maps.maps_reference_data as REFERENCE_DATA
from .forms import CaptureRecordForm
from .models import CaptureRecord
from users.mixins import ApprovalRequiredMixin


def get_band_sizes_for_species(request):
    species_number = request.GET.get("species_number")
    band_sizes = REFERENCE_DATA.SPECIES.get(int(species_number), {}).get("band_sizes", [])
    return JsonResponse({"band_sizes": band_sizes})


class CreateCaptureRecordView(LoginRequiredMixin, ApprovalRequiredMixin, CreateView):
    template_name = "maps/enter_bird.html"
    form_class = CaptureRecordForm

    def get(self, request, *args, **kwargs):
        # Set start time in session when the form is first loaded
        request.session['form_start_time'] = timezone.now().isoformat()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Retrieve start time from session and convert it back to a datetime object
        start_time_str = self.request.session.pop('form_start_time', None)
        start_time = timezone.datetime.fromisoformat(start_time_str)

        submission_time = timezone.now()
        
        # Calculate time held and set it on the instance before saving
        time_held = submission_time - start_time
        form.instance.hold_time = time_held.total_seconds() / 60

        form.instance.user = self.request.user
        form.instance.bander_initials = self.request.user.initials
        self.object = form.save()
        messages.success(self.request, "Capture record created successfully.")
        return redirect(reverse_lazy("maps:detail_capture_record", kwargs={"pk": self.object.pk}))

class DetailCaptureRecordView(LoginRequiredMixin, DetailView):
    template_name = "maps/detail.html"
    model = CaptureRecord
    context_object_name = "capture_record"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        species_info = REFERENCE_DATA.SPECIES[self.object.species_number]
        context["species_name"] = species_info["common_name"]
        return context


class ListCaptureRecordView(LoginRequiredMixin, ListView):
    template_name = "maps/list_all.html"
    model = CaptureRecord
    context_object_name = "capture_records"

    def get_queryset(self):
        return CaptureRecord.objects.filter(user=self.request.user)


class MiniPyleView(TemplateView):
    template_name = "maps/mini_pyle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        species_number = self.kwargs.get("species_number")
        species_info = REFERENCE_DATA.SPECIES.get(species_number, {})
        context.update(
            {
                "species_number": species_number,
                "common_name": species_info.get("common_name", "Unknown"),
                "scientific_name": species_info.get("scientific_name", ""),
                "alpha_code": species_info.get("alpha_code", ""),
                "band_sizes": ", ".join(species_info.get("band_sizes", [])),
                "band_sizes_by_sex": species_info.get("band_sizes_by_sex", None),
                "wing_chord_range": " - ".join(map(str, species_info.get("wing_chord_range", []))),
                "wing_chord_range_by_sex": species_info.get("wing_chord_range_by_sex", None),
                "WRP_groups": ", ".join(map(str, species_info.get("WRP_groups", []))),
                "sexing_criteria": species_info.get("sexing_criteria", {}),
                "pyle_second_edition_page": species_info.get("pyle_second_edition_page", ""),
            },
        )

        return context
