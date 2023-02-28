from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name="rooms"),
    path('<slug:urlRoom>/', views.room, name="room"),
]
