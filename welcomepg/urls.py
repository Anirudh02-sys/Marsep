from django.urls import path

from . import views

urlpatterns = [
    path("",views.login, name='login'),
    path("home",views.home, name='home'),
    path("actmaster",views.actmaster,name='actmaster'),
    path("createnewuser",views.createnewuser, name='createnewuser'),
    path("newact",views.newact,name='newact')
]