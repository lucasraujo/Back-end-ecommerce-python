from rest_framework.serializers import ModelSerializer
from .models import Prize
from user.serializer import UserSerializer


class PrizeSerializer(ModelSerializer):

    class Meta:
        model = Prize
        fields = [
            "id", "name", "numberOfTickets", "description", "pricePerTicket",
            "user", "drawDate", "drawTime"
            ]
        read_only_fields = ["id", "user"]

    user = UserSerializer(read_only=True)