from django.contrib import admin
from .models import Properties, SingleProperty, Contact ,Category

admin.site.register(Properties)
admin.site.register(Contact)
admin.site.register(SingleProperty)
admin.site.register(Category)