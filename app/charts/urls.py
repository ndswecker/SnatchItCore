from django.urls import path

from charts import views

app_name = "charts"

urlpatterns = [
    path(route="", view=views.BirdsView.as_view(), name="birds"),
]
