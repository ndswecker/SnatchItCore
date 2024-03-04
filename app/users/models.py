from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from common.models import BaseModel


class User(AbstractUser, BaseModel):
    is_approved = models.BooleanField(
        "Approval status",
        default=False,
        help_text="Designates whether this user is able to submit capture records.",
    )
    objects = UserManager()
