from django.urls import path 
from . import views

urlpatterns = [
    path("ticket/<int:prize_pk>/", views.TicketView.as_view()),
]