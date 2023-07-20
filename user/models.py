from django.db import models
from django.contrib.auth.models import AbstractUser
from address.models import Address


class User(AbstractUser):
    email = models.CharField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_employee = models.BooleanField(null=True, blank=True, default=False)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name="user",
        primary_key=True,
        )