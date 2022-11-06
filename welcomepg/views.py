from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    return render(request,'dashboard.html')
    
def actmaster(request):
    return render(request,'actmaster.html')

def newact(request):
    return render(request,'newact.html')    

def createnewuser(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name =  request.POST['lname']
        username = request.POST['usr']
        mail_id = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        contact_number = request.POST['telphone']
        typeofusr = request.POST['type value']

        user = User.objects.create_user(username=username,password=password1,email=mail_id,first_name=first_name,last_name=last_name,typeofuser=typeofusr,contact_no=contact_number)
        user.save();
        print('user created!')
        return redirect('/')
    else:
        return render(request,'createnewuser.html')