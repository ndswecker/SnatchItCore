from django.urls import path

from . import views

app_name = "birds"

urlpatterns = [
    path(route="", view=views.TaxonView.as_view(), name="taxons"),
]
