from __future__ import unicode_literals
from django.db import models
from cart.models import Cart
from ecommerce.utils import unique_order_id_generator
from django.db.models.signals import pre_save



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

def pre_save_create_order_id(sender, instance , *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
        
pre_save.connect(pre_save_create_order_id, sender=Order)        
