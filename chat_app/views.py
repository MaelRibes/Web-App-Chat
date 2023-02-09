from django.shortcuts import render
from django.http import HttpResponse
from utils import get_db_handle
import pymongo

def index(request):
    (db_handle, client) = get_db_handle("project","localhost",27017,"","")
    print(db_handle,client)
    dbname = client["project"]
    collection = dbname["Messages"]
    print(collection.find_one())
    return render(request, "chat_app/index.html")

# Create your views here.
