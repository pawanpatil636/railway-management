# Generated by Django 3.1.7 on 2021-04-01 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0004_auto_20210401_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengerdetail',
            name='user',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
