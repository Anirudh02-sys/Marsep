from django.urls import path

from . import views

urlpatterns = [
    path("",views.loginpage, name='login'),
    path("home",views.home, name='home'),
    path("actmaster",views.actmaster,name='actmaster'),
    path("createnewuser",views.createnewuser, name='createnewuser'),
    path("newact",views.newact,name='newact'),
    path("logout",views.logoutpage, name='logout')
]