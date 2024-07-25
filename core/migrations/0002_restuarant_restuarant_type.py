# Generated by Django 5.0.7 on 2024-07-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuarant',
            name='restuarant_type',
            field=models.CharField(choices=[('NE', 'Nepalese'), ('IN', 'Indian'), ('CH', 'Chinese')], default='', max_length=2),
            preserve_default=False,
        ),
    ]
