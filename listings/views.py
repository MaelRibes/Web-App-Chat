from django.shortcuts import render
from django.http import HttpResponse
from utils import get_db_handle
import pymongo

def index(request):
    (db_handle, client) = get_db_handle("WebChat","localhost",27017,"","")
    print(db_handle,client)
    dbname = client["WebChat"]
    collection = dbname["Messages"]
    print(collection.find_one())
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
