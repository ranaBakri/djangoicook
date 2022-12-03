import time
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Categories(models.Model):
    title = models.TextField(max_length=250)
    image = models.ImageField(upload_to="images",blank=True)

    def __str__(self):
        return  (self.title)
    

# Create your models here.

      

class Ingredients(models.Model):
      title= models.TextField()

      def __str__(self):
        return  (self.title)

class Ingredients_Recipes(models.Model):
      ingredient= models.ForeignKey(Ingredients,on_delete=models.CASCADE, related_name="ingred")
      measuretype=models.TextField()
      amount= models.FloatField()

      def __str__(self):
        return  (self.ingredient)
      
      
      


class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipeowner")
    title = models.TextField()
    Description=models.TextField()
    image = models.ImageField()
    serves=models.IntegerField()
    cooktime=models.TextField()
    cat= models.ForeignKey(Categories,on_delete=models.CASCADE, related_name="recipes_cat")

    def __str__(self):
        return  (self.title,self.user)



class Ingredients_Recipes(models.Model):
      ingredient= models.ForeignKey(Ingredients,on_delete=models.CASCADE, related_name="ingred")
      measuretype=models.TextField()
      amount= models.FloatField()
      recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name="recipe",)
      def __str__(self):
        return  (self.ingredient)
      
    
    




class Cookbook(models.Model):
      method=models.TextField()
      recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name="recipe_book",)