from django.shortcuts import render
from Two_App.models import User
# Create your views here.
def users(request):
    users=User.objects.order_by('first_name')
    user_dict={'user_record':users}
    return render(request,'index.html',context=user_dict)