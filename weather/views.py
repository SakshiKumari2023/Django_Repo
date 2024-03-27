from django.shortcuts import render
from weather.models import *
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

def help(request):
    
    return render(request, 'help_and_suggestions.html')