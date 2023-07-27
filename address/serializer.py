from rest_framework.serializers import ModelSerializer
from .models import Address
from user.serializer import UserSerializer


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = ["id", "user", "state", "city", "neighborhood", "street", "houseNumber", "reference", "zipCode"]
        read_only_fields = ["id", "user"]

    user = UserSerializer(read_only=True)
    

