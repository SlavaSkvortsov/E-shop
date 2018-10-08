# Generated by Django 2.1.1 on 2018-09-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180917_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8),
        ),
    ]