# Generated by Django 2.1.1 on 2018-09-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralApp', '0006_auto_20180913_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]
