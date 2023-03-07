from django.urls import path
from . import views

urlpatterns = [
    path("<int:month_number>", views.challenge_by_month_by_number),
    path("<str:month>", views.challenge_by_month, name="challenge_of_the_month"),
    path("", views.index, name="index")
]
