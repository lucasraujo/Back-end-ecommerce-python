from django.db import models


class Ticket(models.Model):
    number = models.PositiveIntegerField()
    prize = models.ForeignKey(
        "prize.Prize", on_delete=models.CASCADE, related_name="tickets"
        )
    userOwner = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="tickets"
        )
    isWinner = models.BooleanField(default=False)