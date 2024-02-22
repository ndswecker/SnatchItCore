
from django.urls import path
from . import views

urlpatterns = [
    path(route='create_record/', view=views.CreateCaptureRecordView.as_view(), name='create_capture_record'),
    path(route='detail_record/', view=views.DetailCaptureRecordView.as_view(), name='detail_capture_record'),
]
