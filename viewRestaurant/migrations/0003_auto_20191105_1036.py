# Generated by Django 2.2 on 2019-11-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewRestaurant', '0002_resid_resname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resid',
            name='resname',
            field=models.CharField(max_length=128),
        ),
    ]
