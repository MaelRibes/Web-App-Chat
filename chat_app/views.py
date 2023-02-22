from django.shortcuts import render
from django.http import HttpResponse
from utils import get_db_handle
import pymongo

def index(request):
    return render(request, 'chat_app/index.html')

def connexion(request):
    return render(request, 'chat_app/connexion.html')

def inscription(request):
        return render(request, 'chat_app/inscription.html')

# Create your views here.
