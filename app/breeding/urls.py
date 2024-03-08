from django.urls import path

from . import views

app_name = "breeding"

urlpatterns = [
    path("", views.ListBreedingRecordView.as_view(), name="list"),
    path("<int:pk>/", views.DetailBreedingRecordView.as_view(), name="detail"),
    path("create/", views.CreateBreedingRecordView.as_view(), name="create"),
]
