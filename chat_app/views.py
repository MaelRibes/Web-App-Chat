import datetime

from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render, redirect
from django_redis import get_redis_connection

from .forms import SignUpForm


def index(request):
    User = get_user_model()
    userArray = (User.objects.all())
    allUsers = set({})
    for users in userArray:
        allUsers.add(users.username)
    nombre_de_connexion = (len(cache.keys("connected_*")))
    arrayOfConnexionUsername = ((cache.keys("connected_*")))
    connectedUsersArray = set({})
    for username in arrayOfConnexionUsername:
        connectedUsersArray.add(username.split('_')[1])

    disconnectedUsersArray = allUsers - connectedUsersArray

    return render(request, 'chat_app/index.html',
                  {'number_of_connexion': nombre_de_connexion, 'connectedUsersArray': connectedUsersArray,
                   'disconnectedUsersArray': disconnectedUsersArray})


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user.username, user)
            cache.set(f"connected_{user.username}", user)  # stocker l'utilisateur dans le cache Redis
            cache.set(f"histo_{datetime.datetime.today()}:{user.username}",
                      user)  # stocker l'utilisateur dans le cache Redis
            return redirect('/')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'chat_app/connexion.html', {'error_message': error_message})
    else:
        return render(request, 'chat_app/connexion.html')


def inscription(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(user.username, user)
            cache.set(f"connected_{user.username}", user)  # stocker l'utilisateur dans le cache Redis
            cache.set(f"histo_{datetime.datetime.today()}:{user.username}",
                      user)  # stocker l'utilisateur dans le cache Redis
            return redirect('/')
        else:
            error_message = form.errors
    else:
        form = SignUpForm()
    return render(request, 'chat_app/inscription.html', {'form': form, 'error_message': error_message})


@login_required
def deconnexion(request):
    redis_conn = get_redis_connection('default')
    redis_conn.delete(f"userSession:1:connected_{request.user}")
    print(request.user)
    logout(request)
    return redirect('/')


def header(request):
    return render(request, 'chat_app/header.html')


def historique(request, user):
    arrayOfHistoUsername = ((cache.keys(f"histo_*{user}")))
    userHistoData = []
    if (arrayOfHistoUsername):
        print(arrayOfHistoUsername)
        for usersData in arrayOfHistoUsername:
            date = usersData.split('_')[1].split(' ')[0]
            time = usersData.split('_')[1].split(' ')[1].replace(f":{user}", '')
            userHistoData.append([date, time])
        print(userHistoData)
    return render(request, 'chat_app/historique.html', {'user': user, 'userHistoData': userHistoData})
