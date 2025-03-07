from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    photoUrl = models.URLField(max_length=200, blank=True, null=True)


