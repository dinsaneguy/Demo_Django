from django import forms

class User_form(forms.Form):
    Username = forms.CharField(max_length=90)
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput())
    Repeat_Password = forms.CharField(widget=forms.PasswordInput())