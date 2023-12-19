from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    confirm_password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    is_golden = models.BooleanField(default=False)
    is_silvern = models.BooleanField(default=False)
