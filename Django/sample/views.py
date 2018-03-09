from django.views import generic
from django.views import View
from .models import Person

class PersonList(generic.TemplateView, View):
    template_name = "sample/sample.html"
    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        person_list = Person.objects.all()
        context['person_list'] = person_list
        return context