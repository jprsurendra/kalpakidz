from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'homeapp/index.html')
