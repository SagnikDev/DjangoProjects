import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen=Faker()
topic=['Search','Social','MarketPlace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        wbpg=WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec=AccessRecord.objects.get_or_create(name=wbpg,date=fake_date)[0]

if __name__=='__main__':
    print('Populating Script')
    populate(10)
    print('Populated Script')