# Generated by Django 3.1.7 on 2021-03-20 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0006_auto_20210320_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trains',
            name='station',
        ),
    ]
