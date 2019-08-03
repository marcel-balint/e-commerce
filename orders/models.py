from __future__ import unicode_literals
from django.db import models
from cart.models import Cart


#dropdown choices - db stored value on left and display value on right 
ORDER_STATUS_CHICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=100, default="created", choices=ORDER_STATUS_CHICES)
    shipping_total = models.DecimalField(default=4.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

