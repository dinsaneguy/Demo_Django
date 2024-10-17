from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.land,name="Landing Page"),
    path("login/",views.login, name="Login Page"),
    path("signup/",views.signup, name="Signup Form")
]
