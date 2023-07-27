from django.db import models


class Prize(models.Model):
    name = models.CharField(max_length=127)
    numberOfTickets = models.IntegerField()
    description = models.TextField()
    pricePerTicket = models.FloatField()
    user = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, related_name="prizes",
        null=True
        )
    drawDate = models.DateField()
    drawTime = models.TimeField()
