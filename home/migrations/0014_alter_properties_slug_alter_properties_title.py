# Generated by Django 5.2.4 on 2025-07-30 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_properties_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
