from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import User_form

# Create your views here.
def land(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    form = User_form()
    return render(request,"/signup.html", {"form":form})