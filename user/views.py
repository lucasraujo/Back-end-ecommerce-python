from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import createOrIsAccontOwner
from .models import User
from .serializer import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [createOrIsAccontOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewId(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [createOrIsAccontOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"