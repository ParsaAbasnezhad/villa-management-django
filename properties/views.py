from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, CreateView
from home.models import *
from properties.forms import *


class PropertiesView(View):
    def get(self, request):
        products = Properties.objects.all()
        return render(request, 'properties/properties.html', {'products': products})

    def post(self, request):
        pass


from django.http import HttpResponseRedirect


class VisitCreateView(CreateView):
    model = Visite
    form_class = VisitForm
    template_name = 'properties/contact.html'
    success_url = reverse_lazy('home:home')
