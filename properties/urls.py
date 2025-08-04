from django.urls import path
from . import views

app_name = 'properties'
urlpatterns = [
    path('propertie/<int:category_id>', views.PropertiesByCategoryView.as_view(), name='products'),
    path('visit/', views.VisitCreateView.as_view(), name='visit'),
    path('property/all/', views.PropertiesView.as_view(), name='property_list')
]
