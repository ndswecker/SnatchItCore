from django.urls import path

from . import views

app_name = "breeding"

urlpatterns = [
    path("station/<str:station>/", views.ReportView.as_view(), name="report"),
    path("status/", views.status_view, name="status"),
]
