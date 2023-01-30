from django.urls import path

from . import views
from .views import SignUpView, AllUsers


urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('AllUsers/', AllUsers, name='AllUsers')
]