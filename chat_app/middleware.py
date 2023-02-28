from django.shortcuts import redirect
from django.urls import reverse


class RedirectAuthenticatedUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path_info)
        if request.user.is_authenticated and request.path_info in [reverse('connexion'), reverse('inscription')]:
            return redirect('index')  # redirect to home page

        response = self.get_response(request)
        return response
