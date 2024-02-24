from typing import Any
from django.views.generic import CreateView, DetailView, ListView
from .forms import CaptureRecordForm
from .models import CaptureRecord

class CreateCaptureRecordView(CreateView):
    template_name = 'maps/enter_bird.html'
    form_class = CaptureRecordForm
    success_url = '/maps/'
    
class DetailCaptureRecordView(DetailView):
    template_name = 'maps/detail.html'
    model = CaptureRecord
    context_object_name = 'capture_record'

class ListCaptureRecordView(ListView):
    template_name = 'maps/list_all.html'
    model = CaptureRecord
    context_object_name = 'capture_records'