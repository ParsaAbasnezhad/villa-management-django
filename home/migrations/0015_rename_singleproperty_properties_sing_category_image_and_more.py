# Generated by Django 5.2.4 on 2025-07-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_properties_slug_alter_properties_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='SingleProperty',
            new_name='sing',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='category/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singleproperty',
            name='active_parking',
            field=models.BooleanField(default=True),
        ),
    ]
