# Generated by Django 3.0.4 on 2020-03-22 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bag',
            name='profile',
        ),
    ]
