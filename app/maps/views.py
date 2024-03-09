from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .forms import CaptureRecordForm
from .models import CaptureRecord
from users.mixins import ApprovalRequiredMixin

from django.http import JsonResponse
import maps.maps_reference_data as REFERENCE_DATA


def get_band_sizes_for_species(request):
    species_number = request.GET.get('species_number')
    band_sizes = REFERENCE_DATA.SPECIES.get(int(species_number), {}).get('band_sizes', [])
    return JsonResponse({'band_sizes': band_sizes})

def get_species(request):
    species_number = request.GET.get('species_number')
    species_info = REFERENCE_DATA.SPECIES.get(int(species_number))  # Convert string to int and get species info

    if species_info:
        # Prepare the data to be sent as JSON
        data = {
            'common_name': species_info['common_name'],
            'scientific_name': species_info['scientific_name'],
            'alpha_code': species_info['alpha_code'],
            'band_sizes': species_info['band_sizes'],
            'wing_chord_range': species_info['wing_chord_range'],
            'WRP_groups': species_info['WRP_groups'],
            'sexing_criteria': species_info['sexing_criteria'],
            'pyle_second_edition_page': species_info['pyle_second_edition_page'],
        }
        return JsonResponse(data)
    else:
        # If species info not found, you can return an error message or empty data
        return JsonResponse({'error': 'Species not found'}, status=404)

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
