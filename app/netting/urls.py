from django.urls import path

from . import views

app_name = "netting"

urlpatterns = [
    path("", views.ListNettingRecordView.as_view(), name="list"),
    path("<int:pk>/", views.DetailNettingRecordView.as_view(), name="detail"),
    path("create/", views.CreateNettingRecordView.as_view(), name="create"),
]
