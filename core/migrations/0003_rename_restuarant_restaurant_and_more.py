# Generated by Django 5.0.7 on 2024-07-25 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_restuarant_restuarant_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restuarant',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='restuarant',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restuarant_type',
            new_name='restaurant_type',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='restuarant',
            new_name='restaurant',
        ),
    ]
