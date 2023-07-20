from django.db import models


class Address(models.Model): 
    id = models.UUIDField(primary_key=True)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=127)
    neighborhood = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    houseNumber = models.CharField(max_length=127)
    reference = models.TextField(null=True)
    zipCode = models.CharField(max_length=12)


