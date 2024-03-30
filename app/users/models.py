from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager
from common.models import BaseModel


class User(AbstractUser, BaseModel):
    initials = models.CharField(max_length=3, null=True, blank=True, unique=True)
    objects = UserManager()
