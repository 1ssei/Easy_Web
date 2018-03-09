from django.contrib import admin
from home import models


class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('date', 'min_temperature', 'max_temperature')


admin.site.register(models.Temperature,TemperatureAdmin)
