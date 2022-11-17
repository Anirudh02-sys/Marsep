from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,acts
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginpage(request):
    if(request.method =='POST'):
        user = authenticate(username=request.POST['u'], password=request.POST['p'])
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'invalid credentials!')
            return redirect('/')
    # No backend authenticated the credentials
    else:
        return(render(request,'loginpage.html'))

def home(request):
    if request.user.is_superuser:
        return render(request,'adminpage.html')
    elif request.user.typeofusr == 'Sub-Contractor':
        return render(request,'subpage.html')
    elif request.user.typeofusr == 'Auditor':
        return render(request,'auditpage.html')
    
def actmaster(request):
    return render(request,'actmaster.html')

def newact(request):
    if (request.method == 'POST'):
        act_name = request.POST['actn']
        act_sname = request.POST['actsn']
        actsdata = acts.objects.create(act_name = act_name, act_shname = act_sname)
        actsdata.save()

        return render(request,'actmaster.html')
    else:
        return render(request,'newact.html')  



def createnewuser(request):
    auditors = User.objects.filter(typeofusr='Auditor')
    context = {'auditors':auditors}
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
        allot = request.POST['allot']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!')
                return redirect('createnewuser')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'E-mail Taken!')
                return redirect('createnewuser')
            else:
                print("hey")
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,typeofusr=typeofusr,contact_number=contact_number)
                user.save()
                '''
                if allot:
                    alloted = Allot.objects.create(contractor= User.objects.filter(username = username))
                    alloted.auditor = User.objects.filter(username = allot)
                    alloted.save()
                messages.success(request,'User Sucessfully created')
                '''
        else:
            messages.info(request,'Password not matching!')
            return redirect('createnewuser')
    
        return redirect('createnewuser')
    else:
        return render(request,'createnewuser.html',context)

def logoutpage(request):
    logout(request)
    return redirect('login')        

