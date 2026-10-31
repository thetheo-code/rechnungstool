from django.urls import path
from . import views

urlpatterns = [
    path("", views.kundenListe, name="Kundenliste")
]
