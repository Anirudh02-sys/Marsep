from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
# Create your views here.
def login(request):
    if(request.method =='POST'):
        user = authenticate(username=request.POST['u'], password=request.POST['p']);
        if user is not None:
            return redirect('/home')
        else:
            messages.info(request,'invalid credentials!')
            return redirect('/')
    # No backend authenticated the credentials
    else:
        return(render(request,'loginpage.html'))

def home(request):
    return render(request,'dashboard.html')
    
def actmaster(request):
    return render(request,'actmaster.html')

def newact(request):
    return render(request,'newact.html')    

def createnewuser(request):

    if (request.method == 'POST'):
        print(request.POST['choose'])
        first_name = request.POST['fname']
        last_name =  request.POST['lname']
        username = request.POST['usr']
        email = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        contact_number = request.POST['telphone']
        typeofusr = request.POST['choose']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!')
                return redirect('createnewuser')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'E-mail Taken!')
                return redirect('createnewuser')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,typeofusr=typeofusr,contact_number=contact_number)
                user.save();
                print("user created!")
        else:
            messages.info(request,'Password not matching!')
            return redirect('createnewuser')
    
        return redirect('/')
    else:
        return render(request,'createnewuser.html')