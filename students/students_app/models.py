from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=256)
    middle_name=models.CharField(max_length=256,blank=True)
    last_name=models.CharField(max_length=256)
    fathers_name=models.CharField(max_length=256)
    address=models.TextField(max_length=256)
    department=models.CharField(max_length=256)
    passing_year=models.DurationField()
    roll_no=models.IntegerField()
    email=models.EmailField(max_length=254)
    phone_number=models.IntegerField()
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse("students_app:detail", kwargs={"pk": self.pk})
    