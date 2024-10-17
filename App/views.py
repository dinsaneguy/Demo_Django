from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import User_form
from .models import Users

# Create your views here.
def land(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

    

def signup(request):
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['uname']
            mail = form.cleaned_data['umail']
            passwd = form.cleaned_data['upwd']
            pass_rpt = form.cleaned_data['upwd_repeat']
            theuser = Users.objects.create(username=name, email=mail, password=passwd)
            theuser.save()
            return render(request,"login.html")
    form = User_form()
    return render(request,"signup.html", {"form":form})