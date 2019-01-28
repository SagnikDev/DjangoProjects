from django.conf.urls import url
from . import views

app_name='students_app'

urlpatterns=[
    url(r'^register$',views.register,name='register'),
    url(r'^register_ack$',views.register_ack,name='register_ack'),
    url(r'^logout$',views.logout_user,name='logout'),
    url(r'^index$',views.StudentListView.as_view(),name='index'),
    url(r'^student_register',views.StudentCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',views.StudentDetailView.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)/$',views.StudentUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='delete'),
]