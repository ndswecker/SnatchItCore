from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

from breeding.forms import BreedingRecordForm
from breeding.models import BreedingRecord


class CreateBreedingRecordView(FormView):
    template_name = "breeding/create.html"
    form_class = BreedingRecordForm
    success_url = reverse_lazy("breeding:create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ListBreedingRecordView(ListView):
    model = BreedingRecord
    template_name = "breeding/list.html"
    context_object_name = "records"

    def get_queryset(self):
        return BreedingRecord.objects.filter(user=self.request.user)


class DetailBreedingRecordView(DetailView):
    model = BreedingRecord
    template_name = "breeding/detail.html"
    context_object_name = "record"
