from typing import Any
from django.views.generic import CreateView, DetailView
from .forms import CaptureRecordForm
from .models import CaptureRecord

class CreateCaptureRecordView(CreateView):
    template_name = 'maps/enter_bird.html'
    form_class = CaptureRecordForm
    success_url = '/maps/'

class DetailCaptureRecordView(DetailView):
    template_name = 'maps/capture_record.html'
    model = CaptureRecord
    