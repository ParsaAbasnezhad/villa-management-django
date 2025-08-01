# Generated by Django 5.2.4 on 2025-07-27 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_properties_about_singleproperty_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='apartment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='home.properties'),
        ),
        migrations.AlterField(
            model_name='category',
            name='penthouse',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penthouse', to='home.properties'),
        ),
        migrations.AlterField(
            model_name='category',
            name='villa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='villa', to='home.properties'),
        ),
    ]
