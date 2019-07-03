from django.db import models
from django.contrib.auth.models import User


class ConsultantProfile (models.Model):
    consultant = models.OneToOneField(
        User, on_delete=models.SET_NULL, blank=False, null=True)


class University (models.Model):
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField()