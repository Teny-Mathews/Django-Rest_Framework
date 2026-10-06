from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=20)
    meal_type=models.CharField(max_length=20)
    cusine=models.CharField(max_length=20)
    ingredents=models.TextField()
    instructions=models.TextField()
    image=models.ImageField(upload_to="recipe",null=True)


