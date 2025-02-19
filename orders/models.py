from django.db import models
from django.conf import settings
from shop.models import Product
from django.urls import reverse
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon

class Order(models.Model):
    coupon = models.ForeignKey(Coupon,
                                related_name='orders',
                                null=True,
                                blank=True, on_delete=models.PROTECT)
    discount = models.IntegerField(default=0,
                                    validators=[MinValueValidator(0),
                                                MaxValueValidator(100)])
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

    def get_absolute_url(self):
        return reverse('orders:order_detail',
                        args=[self.id])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', null=True, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price
