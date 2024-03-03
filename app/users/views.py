from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = "users/profile.html"
