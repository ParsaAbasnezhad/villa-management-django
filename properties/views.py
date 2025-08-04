from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, View
from properties.models import *
from properties.forms import *
from home.models import *


def properties_by_category(request, category_id):
    categorys = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    properties = Properties.objects.filter(category=category, category__active=True)
    return render(request, 'properties/properties.html', {
        'category': category,
        'properties': properties,
        'categorys': categorys,
    })



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


