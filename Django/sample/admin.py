from django.contrib import admin
from sample.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','birthday')

admin.site.register(Person,PersonAdmin)