from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path(route="profile/", view=views.ProfileView.as_view(), name="profile"),
    path(route="email/change/", view=views.EmailChangeView.as_view(), name="email_change"),
]
