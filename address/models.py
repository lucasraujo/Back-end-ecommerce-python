from django.db import models


class Address(models.Model): 
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=127)
    neighborhood = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    houseNumber = models.CharField(max_length=127)
    reference = models.TextField(null=True)
    zipCode = models.CharField(max_length=12)
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="address",
        null=True
        )
