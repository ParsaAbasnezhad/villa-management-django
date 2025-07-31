from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,  CreateView
from home.models import *
from properties.forms import *


class PropertiesView(ListView):
    queryset = Properties.objects.all()
    context_object_name = 'properties'
    paginate_by = 1
    template_name = 'properties/properties.html'


class VisitCreateView(CreateView):
    model = Visite
    form_class = VisitForm
    template_name = 'properties/contact.html'
    success_url = reverse_lazy('home:home')
