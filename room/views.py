from django.shortcuts import render
from .models import Room
from utils import get_db_handle
from .forms import MessageForm
from datetime import datetime

(db_handle, client) = get_db_handle()
db = client["WebChat"]


def rooms(request):
    rooms = Room.objects.all()
    collection = db["Room"]
    return render(request, 'room/rooms.html', {'rooms': collection.find()})


def room(request, urlRoom):
    collectionRoom = db["Room"]
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print(form)
        if form.is_valid():
            collectionMessages = db["Messages"]
            form = form.cleaned_data
            form["username"] = request.user.username
            form["date"] = datetime.now().strftime("%-d/%-m/%Y %H:%M:%S")
            form["room"] = collectionRoom.find_one({"name": urlRoom})["_id"]
            collectionMessages.insert_one(form)

    room = collectionRoom.find_one({"name": urlRoom})
    collectionMessages = db["Messages"]
    messages = collectionMessages.find({"room": room["_id"]})
    form = MessageForm()
    return render(request, 'room/room.html', {'room': room, "messages": messages, 'form': form, "username": request.user.username})
