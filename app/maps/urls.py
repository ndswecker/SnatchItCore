from django.urls import path

from . import views
from .views import get_band_sizes_for_species

app_name = "maps"

urlpatterns = [
    path(route="create_record/", view=views.CreateCaptureRecordView.as_view(), name="create_capture_record"),
    path(route="detail_record/<int:pk>/", view=views.DetailCaptureRecordView.as_view(), name="detail_capture_record"),
    path(route="", view=views.ListCaptureRecordView.as_view(), name="list_capture_records"),
    path(route="get_band_sizes_for_species/", view=get_band_sizes_for_species, name="get_band_sizes_for_species"),
    path(route="mini_pyle/<int:species_number>/", view=views.MiniPyleView.as_view(), name="mini_pyle"),
    path(route="edit_record/<int:pk>/", view=views.EditCaptureRecordView.as_view(), name="edit_capture_record"),
]
