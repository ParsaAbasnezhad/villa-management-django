

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView ,ListView

from home.models import Properties


class PropertiesView(ListView):
    queryset = Properties.objects.all()
    context_object_name = 'properties'
    template_name = 'home/index.html'


