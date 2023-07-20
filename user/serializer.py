from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(ModelSerializer):

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that email already exists."
            )
        ]
    )

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists."
            )
        ]
    )

    extra_kwargs = {"password": {"write_only": True}}

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
        ]

        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
