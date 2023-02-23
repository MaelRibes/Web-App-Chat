from django.shortcuts import render
from .models import Room
from utils import get_db_handle
from .forms import MessageForm

(db_handle, client) = get_db_handle()
dbname = client["WebChat"]

def rooms(request):
    rooms = Room.objects.all()
    collection = dbname["Room"]
    return render(request, 'room/rooms.html', {'rooms': collection.find() })


def room(request,urlRoom):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            collectionMessages = dbname["Messages"]
            form = form.cleaned_data
            collectionMessages.insert_one(form)
            print(form)
            
    collectionRoom = dbname["Room"]
    room = collectionRoom.find_one({"name": urlRoom})
    collectionMessages = dbname["Messages"]
    messages = collectionMessages.find({"name":urlRoom})
    form = MessageForm()
    return render(request, 'room/room.html', {'room': room, "messages" : messages, 'form' : form})