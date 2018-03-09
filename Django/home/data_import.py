'''
import os,sys,django
os.chdir("../Django")
dhome = os.getcwd()
sys.path.append(dhome)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
'''
import home.models
import random
import datetime
from datetime import timedelta


def importData():
    home.models.Temperature.objects.all().delete()
    start_date = datetime.datetime(2018, 1, 1, 0, 0, 0, 0)
    day_count = 365
    datas = []
    for target_date in (start_date + timedelta(n) for n in range(day_count)):
        max_temperature =random.randint(20, 30)
        min_temperature =random.randint(1, 10)
        datas.append(
            home.models.Temperature(date = target_date,max_temperature=max_temperature,min_temperature=min_temperature))
    home.models.Temperature.objects.bulk_create(datas)

#importData()