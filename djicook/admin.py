from django.contrib import admin
from .models import Categories,Ingredients,Recipes,Ingredients_Recipes
# Register your models here.
admin.site.register([Categories,Ingredients,Recipes,Ingredients_Recipes])