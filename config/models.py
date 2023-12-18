from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_golden = models.BooleanField(default=False)
    is_silvern = models.BooleanField(default=False)

