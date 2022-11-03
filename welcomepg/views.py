from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'dashboard.html')
    
def actmaster(request):
    return render(request,'actmaster.html')
