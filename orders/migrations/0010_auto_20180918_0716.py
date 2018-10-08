# Generated by Django 2.1.1 on 2018-09-18 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_price'),
        ('orders', '0009_remove_productinorder_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(default=1488, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]