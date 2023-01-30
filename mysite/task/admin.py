from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUser
    list_display = ["email", "username",]

admin.site.register(MyUser, MyUserAdmin)