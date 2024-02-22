from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from common.models import BaseModel


class User(AbstractUser, BaseModel):
    objects = UserManager()
