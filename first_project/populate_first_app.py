
import django
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
# settings.configure()

django.setup()


## Fake Population Script

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():

    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

    # all_entries = Topic.objects.all()[0]
    # print(all_entries)

def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create the fake databases
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create fake access record

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(400)
    # print(settings.DATABASES)
    print("Completed.")
    pass
