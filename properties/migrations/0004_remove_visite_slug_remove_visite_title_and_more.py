# Generated by Django 5.2.4 on 2025-07-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_visite_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visite',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='visite',
            name='title',
        ),
        migrations.AddField(
            model_name='visite',
            name='subject',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
