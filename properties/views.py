from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, View
from properties.models import *
from properties.forms import *
from home.models import *


class PropertiesByCategoryView(ListView):
    model = Properties
    template_name = 'properties/properties.html'
    context_object_name = 'properties'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Properties.objects.filter(category=self.category, category__active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categorys'] = Category.objects.all()
        return context

class PropertiesView(ListView):
    model = Properties
    template_name = 'properties/properties.html'
    context_object_name = 'all_properties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context



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
