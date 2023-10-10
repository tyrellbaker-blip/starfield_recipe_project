# Generated by Django 4.2.6 on 2023-10-10 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipeingredient_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='crafted_from',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.category'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
