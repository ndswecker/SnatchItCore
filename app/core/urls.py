from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

admin.site.login = staff_member_required(
    admin.site.login,
    login_url=settings.LOGIN_URL,
)

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("breeding/", include("breeding.urls"), name="breeding"),
    path("charts/", include("charts.urls"), name="charts"),
    path("maps/", include("maps.urls"), name="maps"),
    path("netting/", include("netting.urls"), name="netting"),
    path("users/", include("users.urls"), name="users"),
]
