from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreationForm
from .models import MyUser

def index(request):
    return HttpResponse("Hello world!")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def AllUsers(request):
    users_list = MyUser.objects.all()

    context = {
            "users_list": users_list,
            "username": MyUser.username,
        }
    return render(request, 'AllUsers.html', context)