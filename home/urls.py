from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('home/', views.PropertiesView.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('detail/<slug:slug>/', views.PropertyDetailViews.as_view(), name='detail'),

]
