from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
from django.utils import timezone
from django.views.generic import TemplateView

from breeding.forms import StatusForm
from breeding.models import Status
from maps.maps_reference_data import BREEDING_STATUSES
from maps.maps_reference_data import SPECIES


class ReportView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = "maps.view_capturerecord"
    template_name = "breeding/report.html"

    def _get_table(self, station):
        """Create a representation of the HTML table as nested dicts.
        Populates periods for species in which status record exist.

        {
            "SOSP": {1: "Cn", ..., 10: "--"},
            "OCWA": {1: "--", ..., 10: "Ps"},
            ...,
        }
        """

        table = {}
        absent_string = "--"
        species_list = [SPECIES[s]["alpha_code"] for s in sorted(SPECIES)]
        for species in species_list:
            table[species] = {i: absent_string for i in range(1, 11)}
        for status in Status.objects.filter(created_at__year=timezone.now().year, station=station):
            table[status.species][status.period] = status.status
        return table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["station"] = self.kwargs["station"]
        context["table"] = self._get_table(station=self.kwargs["station"])
        context["options"] = BREEDING_STATUSES.keys()
        return context


@login_required
@permission_required("maps.add_capturerecord")
def status_view(request):
    if request.method == "POST":
        form = StatusForm(data=request.POST)
        if form.is_valid():
            existing_status = Status.objects.filter(
                species=form.cleaned_data["species"],
                period=form.cleaned_data["period"],
                station=form.cleaned_data["station"],
            ).first()
            if existing_status:
                existing_status.status = form.cleaned_data["status"]
                existing_status.user = request.user
                existing_status.save()
            else:
                form.instance.user = request.user
                form.save()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse(
                {
                    "status": "error",
                    "errors": form.errors,
                },
            )
    return HttpResponseNotAllowed(["POST"])
