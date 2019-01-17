import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PreojectTwo.settings')

import django
django.setup()
from faker import Faker
from Two_App.models import User

fakegen=Faker()

def Population(n=5):
    for entry in range(n):
        name=fakegen.name().split()
        f_first_name=name[0]
        f_last_name=name[1]
        f_email=fakegen.email()

        user=User.objects.get_or_create(first_name=f_first_name,last_name=f_last_name,email=f_email)[0]

if __name__=='__main__':
    print('Populatin Creating')
    Population(50)
    print('Population Created')
