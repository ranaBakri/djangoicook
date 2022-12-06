from django.contrib import admin
from .models import Categories,Recipes
# Register your models here.
admin.site.register([Categories,Recipes])