# Generated by Django 3.1.7 on 2021-03-31 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger_details',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='passenger_details',
            name='last_name',
        ),
    ]