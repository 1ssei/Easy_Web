from django.views import generic
from django.views import View
from home import calc4graph
from home import data_import

class Home(generic.TemplateView, View):
    template_name = "home/home.html"
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['highstock'] = calc4graph.make_graph()
        return context

