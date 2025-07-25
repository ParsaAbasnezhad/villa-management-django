from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView

from home.models import Properties, Contact


class PropertiesView(ListView):
    queryset = Properties.objects.all()
    context_object_name = 'properties'
    template_name = 'home/index.html'


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
