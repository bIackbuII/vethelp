# Generated by Django 2.2.16 on 2022-01-24 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='slug',
        ),
    ]
