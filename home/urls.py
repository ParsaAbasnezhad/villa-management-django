from django.urls import path
from . import views
from .views import PropertiesView

app_name = 'home'
urlpatterns = [
    path('home/', PropertiesView.as_view(), name='home'),
]
