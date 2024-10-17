from django import forms
from .models import Users

class User_form(forms.Form):
    uname = forms.CharField(max_length=90),
    umail = forms.EmailField()
    upwd = forms.PasswordInput()
    upwd_repeat = forms.PasswordInput()