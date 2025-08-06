from django.shortcuts import render, redirect
from django.views.generic import  ListView
from django.views.generic.detail import DetailView
from home.models import *


class PropertiesView(ListView):
    queryset = Properties.objects.order_by('-id')[:3]
    context_object_name = 'properties'
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


def contact(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(fullname=fullname, email=email, subject=subject, message=message)
        return redirect('home:home')
    else:
        return render(request, 'home/index.html')


class PropertyDetailViews(DetailView):
    model = Properties
    context_object_name = 'details'
    template_name = 'home/detail.html'
    slug_url_kwarg = 'slug'


