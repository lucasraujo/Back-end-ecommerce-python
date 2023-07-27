from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Prize
from .serializer import PrizeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PrizeView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)