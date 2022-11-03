from django.urls import path
#from .models import User
from . import views

#usr1 = User()

urlpatterns = [
    path('',views.login, name='login')
]