from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("maps/", include("maps.urls"), name="maps"),
    path("users/", include("users.urls"), name="users"),
]
