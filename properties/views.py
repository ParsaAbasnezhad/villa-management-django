from django.shortcuts import render
from django.views.generic import TemplateView, ListView ,View
from home.models import *

class PropertiesView(View):
    def get(self, request):
        products= Properties.objects.all()
        return render(request, 'properties/properties.html',{'products':products})

    def post(self,request):
        pass
