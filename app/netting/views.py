from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView

from netting.forms import NettingRecordForm
from netting.models import NettingRecord


class CreateNettingRecordView(FormView):
    template_name = "netting/create.html"
    form_class = NettingRecordForm
    success_url = reverse_lazy("netting:create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ListNettingRecordView(ListView):
    model = NettingRecord
    template_name = "netting/list.html"
    context_object_name = "netting_records"

    def get_queryset(self):
        return NettingRecord.objects.filter(user=self.request.user)


class DetailNettingRecordView(DetailView):
    model = NettingRecord
    template_name = "netting/detail.html"
    context_object_name = "record"
