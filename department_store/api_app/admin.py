from django.contrib import admin
from .models import Items, Suppliers, Category

admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Suppliers)
