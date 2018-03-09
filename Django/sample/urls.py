from django.conf.urls import url
from . import views

app_name = 'sample'
urlpatterns = [
    url(r'^person_list/?$', view=views.PersonList.as_view(), name='person_list'),
]