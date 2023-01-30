from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MyUser

class UserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ("username", "email")

class UserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ("username", "email")