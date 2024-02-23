
from django.urls import path
from . import views
app_name = 'maps'

urlpatterns = [
    path(route='create_record/', view=views.CreateCaptureRecordView.as_view(), name='create_capture_record'),
    path(route='detail_record/<int:pk>/', view=views.DetailCaptureRecordView.as_view(), name='detail_capture_record'),
    path(route='', view=views.ListCaptureRecordView.as_view(), name='list_capture_records'),
]
