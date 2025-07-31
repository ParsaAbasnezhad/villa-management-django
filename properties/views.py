from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, View
from properties.models import *
from properties.forms import *
from home.models import *



class PropertiesView(ListView):
    queryset = Properties.objects.all()
    context_object_name = 'properties'
    paginate_by = 1
    template_name = 'properties/properties.html'


# class VisitCreateView(CreateView):
#     model = Visite
#     form_class = VisitForm
#     template_name = 'properties/contact.html'
#     success_url = reverse_lazy('home:home')


class VisitCreateView(View):
    def get(self, request):
        title = request.GET.get('title')
        request.session['title'] = title
        return render(request, 'properties/contact.html', {'title': title})

    def post(self, request):
        title = request.session.get('title')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        Visite.objects.create(
            title=title,
            full_name=full_name,
            email=email,
            number=number,
            message=message,
            subject=subject)
        return redirect('home:home')
