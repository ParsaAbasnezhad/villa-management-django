from django.contrib import admin
from unicodedata import category

from .models import Properties, SingleProperty, Contact ,Category


admin.site.register(Contact)
admin.site.register(SingleProperty)



@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title','city','category')
    list_filter = ('title','city','category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','active')
    search_fields = ('title',)