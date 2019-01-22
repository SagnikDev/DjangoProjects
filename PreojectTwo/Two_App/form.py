from django import forms
from django.core import validators
from Two_App.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields="__all__"



# class UserForm(forms.Form):
#     f_name=forms.CharField()
#     l_lame=forms.CharField()
#     email=forms.EmailField()
#     verify_email=forms.EmailField(label="Rewrite Email")
#     botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

#     def clean(self):
#         clean_all_data=super().clean()
#         email=clean_all_data['email']
#         vemail=clean_all_data['verify_email']
#         if email != vemail:
#             raise form.ValidationError('Make Sure Email will Same')