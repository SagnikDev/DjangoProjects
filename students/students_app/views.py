from django.shortcuts import render
from students import urls
from .forms import user_form,user_registration_form
from django.contrib.auth.models import User
from . import models
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View,TemplateView,ListView,DetailView,
CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
# Create your views here.
# @login_required
# def index(request):
#     return render(request,'students_app/student_list.html',{})
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('students_app:index'))
        else:
            print('Someone want to login and fail!!')
            print("Username: {} and Password {} ".format(username,password))
            return HttpResponse("Invalid login details!!")
    else:
        form=user_form()
        return render(request,'students_app/user_login.html',{'forms':form})    
def register(request):
    form2=user_registration_form()
    return render(request,'students_app/user_registration.html',{'forms2':form2})   
def register_ack(request):
    if request.method=='POST':
        user_form=user_registration_form(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            print(user_form.errors)
    else:
        return register(request)
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('students_app:index'))

class StudentCreateView(CreateView):
    fields="__all__"
    model=models.Student
class StudentListView(LoginRequiredMixin,ListView):
    model=models.Student
class StudentDetailView(LoginRequiredMixin,DetailView):
    model=models.Student
    template_name='students_app/student_detail.html'
class StudentUpdateView(LoginRequiredMixin,UpdateView):
    fields=('address','department','passing_year','roll_no','phone_number','profile_pic')
    model=models.Student
class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model=models.Student
    success_url=reverse_lazy("students_app:index")
    template_name='students_app/student_confirm_delete.html'