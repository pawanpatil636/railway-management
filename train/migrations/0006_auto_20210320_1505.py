# Generated by Django 3.1.7 on 2021-03-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0005_auto_20210320_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='destination',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trains',
            name='source',
            field=models.CharField(max_length=200),
        ),
    ]
