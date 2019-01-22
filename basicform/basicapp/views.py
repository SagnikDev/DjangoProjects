from django.shortcuts import render
from basicapp import forms
# Create your views here.
def index(request):
    return render(request,'basicform/index.html')

def form_name_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        
        if form.is_valid():
            print("Validation Success")
            print('Name'+form.cleaned_data['name'])
            print('Email'+form.cleaned_data['email'])
            print('Text'+form.cleaned_data['text'])
    form_dir={'forms':form}
    return render(request,'basicform/form_page.html',form_dir)