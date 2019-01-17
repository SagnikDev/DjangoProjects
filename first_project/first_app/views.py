from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord
# Create your views here.
def index(request):
    my_dict={'insert_me':"Hello Its comming from views.py"}
    return render(request,'first_app/index.html',context=my_dict)
def sagnik(request):
    return HttpResponse("<b>Sagnik</b>")
def database(request):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpage_list}
    return render(request,'first_app/index2.html',context=date_dict)