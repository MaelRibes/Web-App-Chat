from django.shortcuts import render
from .models import Room
from utils import get_db_handle


def rooms(request):
    rooms = Room.objects.all()

    (db_handle, client) = get_db_handle()
    dbname = client["WebChat"]
    collection = dbname["Room"]

    return render(request, 'room/rooms.html', {'rooms': collection.find()})


def room(request, urlRoom):
    (db_handle, client) = get_db_handle()
    dbname = client["WebChat"]
    collectionRoom = dbname["Room"]
    room = collectionRoom.find_one({"name": urlRoom})
    collectionMessages = dbname["Messages"]
    messages = collectionMessages.find({"name": urlRoom})
    return render(request, 'room/room.html', {'room': room, "messages": messages})

# Create your views here.
