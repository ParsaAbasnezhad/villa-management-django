from django.urls import path
from . import views

app_name = 'properties'
urlpatterns = [
    path('propertie/<int:category_id>', views.properties_by_category, name='products'),
    path('visit/', views.VisitCreateView.as_view(), name='visit'),
]
