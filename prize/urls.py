from django.urls import path
from . import views

urlpatterns = [
    path("prize/", views.PrizeView.as_view()),
]
