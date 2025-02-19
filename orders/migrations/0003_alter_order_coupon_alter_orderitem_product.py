# Generated by Django 5.0.7 on 2024-07-17 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
        ('orders', '0002_order_coupon_order_discount'),
        ('shop', '0002_product_available_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='coupons.coupon'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='shop.product'),
        ),
    ]
