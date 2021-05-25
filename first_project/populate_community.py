
import django
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
# settings.configure()

django.setup()


## Fake Population Script

import random
from community.models import Human
from faker import Faker

fakegen = Faker()

def add_human(N=5):
    for entry in range(N):
        individual = Human.objects.get_or_create(last_name=fakegen.last_name(), first_name=fakegen.first_name(),email=fakegen.free_email())[0]

    # all_entries = Topic.objects.all()[0]
    # print(all_entries)

if __name__ == '__main__':
    print("Populating script!")
    add_human(100)
    # print(settings.DATABASES)
    print("Completed.")
    pass
