# Generated by Django 4.1.3 on 2022-12-03 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("djicook", "0002_alter_categories_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredients_recipes",
            name="title",
        ),
        migrations.AddField(
            model_name="recipes",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipeowner",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="cookbook",
            name="recipe",
        ),
        migrations.AlterField(
            model_name="ingredients_recipes",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ingred",
                to="djicook.ingredients",
            ),
        ),
        migrations.RemoveField(
            model_name="ingredients_recipes",
            name="recipe",
        ),
        migrations.AlterField(
            model_name="recipes",
            name="cooktime",
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name="cookbook",
            name="recipe",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe_book",
                to="djicook.recipes",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ingredients_recipes",
            name="recipe",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe",
                to="djicook.recipes",
            ),
            preserve_default=False,
        ),
    ]
