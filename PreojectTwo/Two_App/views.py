from django.shortcuts import render
from Two_App.models import User
from Two_App import form
# Create your views here.
def users(request):
    users=User.objects.order_by('first_name')
    user_dict={'user_record':users}
    return render(request,'index.html',context=user_dict)
def sign_up(request):
    forms=form.UserForm()

    if request.method =='POST':
        form2=form.UserForm(request.POST)
        if form2.is_valid():
            form2.save(commit=True)
            return users(request)
        else:
            print("Error From Invalid")
    form_dir={'forms':forms}
    return render(request,'signup.html',form_dir)