# Generated by Django 2.1.1 on 2018-09-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180917_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]