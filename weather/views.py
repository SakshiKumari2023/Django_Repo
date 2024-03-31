from django.shortcuts import render,redirect
from weather.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
# Create your views here.
def home(request):
    history_entries = history.objects.all()
    context = {
        'history_entries': history_entries
    }
    return render(request, 'index.html',context)

def skill_set(request):
    skill_entries = skills.objects.all()
    context1 = {
        'skill_entries': skill_entries
    }
    return render(request, 'skills.html',context1)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User.objects.filter(username=username)
        if not user.exists():
            messages.info(request,'Username is already taken')
            return redirect('/register/')
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        # Redirect to the login page
        return redirect('/register/')
    else:
        return render(request,'register.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        if not user.exists():
            messages.info(request,'User does not exist!')
            return redirect('/login/')

        user=authenticate(username=username, password=password)
        if user is None:
            messages.info(request,'Password incorrect!')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/help_and_suggestions')
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def help(request):
    
    return render(request, 'help_and_suggestions.html')