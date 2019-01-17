from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return HttpResponse("<em>My Second App</em>")
def help(request):
    message={'help_message':"This is a Help Message from AppTwoViews"}
    return render(request,'help.html',context=message)