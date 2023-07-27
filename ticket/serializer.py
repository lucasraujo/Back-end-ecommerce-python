from rest_framework.serializers import ModelSerializer
from .models import Ticket
from user.serializer import UserSerializer
from prize.serializer import PrizeSerializer


class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = ["id", "number", "prize", "userOwner"]
        read_only_fields = ["id", "prize", "userOwner"]

    prize = PrizeSerializer(read_only=True)
    userOwner = UserSerializer(read_only=True)

    def create(self, validated_data):
        NumberInUse = Ticket.objects.filter(
            number=validated_data["number"]
            ).exists()
        if NumberInUse:
            raise Exception("this number has already been taken")
        return super().create(validated_data)