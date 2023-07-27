from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Ticket
from .serializer import TicketSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from prize.models import Prize
from django.shortcuts import get_object_or_404


class TicketView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        prizeQueryset = get_object_or_404(Prize, id=self.kwargs["prize_pk"])
        return serializer.save(
            userOwner=self.request.user, prize=prizeQueryset
            )