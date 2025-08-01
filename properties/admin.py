from django.contrib import admin
from .models import Visite



@admin.register(Visite)
class VisiteAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('phone', 'title')
    list_filter = ('full_name','title')


