from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("connexion/", views.connexion, name="connexion"),
    path("inscription/", views.inscription, name="inscription"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),

]
