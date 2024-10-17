from django import forms

class User_form(forms.Form):
    uname = forms.CharField(max_length=90)
    umail = forms.EmailField()
    upwd = forms.CharField(widget=forms.PasswordInput())
    upwd_repeat = forms.CharField(widget=forms.PasswordInput())


# class User_form(forms.Form):
#     uname = forms.CharField(max_length=90),
#     umail = forms.EmailField()
#     upwd = forms.PasswordInput()
#     upwd_repeat = forms.PasswordInput()