import sys, os
import django
from datetime import datetime, timezone

#omajinai if you run in local(run this file ) , please remove '''
'''
os.chdir("../Django")
dhome = os.getcwd()
sys.path.append(dhome)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
'''
#you can edit from here
from sample.models import Person


def loadPerson():
    person = Person(name='test',birthday=datetime.strptime('1993-01-27', '%Y-%m-%d'))
    person.save()

#loadPerson()#if you want to test , please run this line