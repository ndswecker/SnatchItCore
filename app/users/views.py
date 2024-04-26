from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import TemplateView

from users.forms import EmailChangeForm
from users.forms import FirstLastSignupForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"


class EmailChangeView(LoginRequiredMixin, FormView):
    template_name = "users/change_email.html"
    form_class = EmailChangeForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        self.request.user.email = form.cleaned_data["email"]
        self.request.user.save()
        messages.success(self.request, "Your email has been updated.")
        return super().form_valid(form)
