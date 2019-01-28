from django import forms
from django.contrib.auth.models import User

class user_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password')
class user_registration_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password')