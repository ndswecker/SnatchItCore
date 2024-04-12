from django.urls import path

from charts import views

app_name = "charts"

urlpatterns = [
    path(route="birds/", view=views.BirdsView.as_view(), name="birds"),
    path(route="species/", view=views.NetsView.as_view(), name="nets"),
]
