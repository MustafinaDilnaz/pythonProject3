from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from rest_framework import routers, serializers, viewsets

class MyUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(verbose_name='email address',
    #     max_length=255,
    #     unique=True,)
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    # isSuperUser = forms.BooleanField
    pass

    def __str__(self):
        return self.username


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = MyUser

router = routers.DefaultRouter()
# router.register(r'users', MyUser)

