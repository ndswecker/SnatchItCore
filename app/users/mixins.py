from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


class ApprovalRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_approved:
            messages.error(request, "This account is not yet approved. Request approval from an administrator.")
            return HttpResponseRedirect(reverse("users:profile"))
        return super().dispatch(request, *args, **kwargs)
