from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth import logout
from django_redis import get_redis_connection


def index(request):
    return render(request, 'chat_app/index.html')


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user.username, user)
            cache.set("Connected " + user.username, user)  # stocker l'utilisateur dans le cache Redis
            return render(request, 'chat_app/index.html')
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
            cache.set(user.username, user)  # stocker l'utilisateur dans le cache Redis
            return render(request, 'chat_app/index.html')
        else:
            error_message = form.errors
    else:
        form = SignUpForm()
    return render(request, 'chat_app/inscription.html', {'form': form, 'error_message': error_message})


@login_required
def deconnexion(request):
    redis_conn = get_redis_connection('default')
    redis_conn.delete(f"userSession:1:Connected {request.user}")
    print(request.user)
    logout(request)
    return render(request, 'chat_app/index.html')
