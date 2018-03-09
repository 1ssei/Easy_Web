from django.db import models

class Temperature(models.Model):
    date =  models.DateTimeField('date')
    max_temperature = models.IntegerField(default=0)
    min_temperature = models.IntegerField(default=0)
    def __str__(self):
        return self.date
