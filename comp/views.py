from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products,address
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import date

# Create your views here.
def home(request):
    pr=products.objects.all()
    return render(request,'index.html',{'pr':pr})
def register(request):
    if request.method=='POST':
        f_n=request.POST['fname']
        l_n=request.POST['lname']
        user_n=request.POST['username']
        passw=request.POST['password']
        if User.objects.filter(username=user_n).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
            
        else:
            user=User.objects.create_user(username=user_n,password=passw,first_name=f_n,last_name=l_n)
            user.save()
            return render(request,'login.html')
    else:
        return render(request,'register.html')

   
def login(request):
    if request.method=='POST':
        user=request.POST['usernam']
        passw=request.POST['passwor']

        user=auth.authenticate(username=user,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
def buy(request,prod):
    if request.method=="POST":

        ob=address()
        ob.name=request.user
        ob.product=prod
        ob.date=date.today()
        ob.street=request.POST['street']
        ob.city=request.POST['city']
        ob.state=request.POST['state']
        ob.pincode=request.POST['pincode']
        ob.cell=request.POST['cell']
        ob.save()
        return redirect('home')
    else:
        s=prod
        return render(request,'buy.html',{'s':s})

def order(request):
    l=address.objects.filter(name=str(request.user))

    return render(request,'orders.html',{'pr':l})