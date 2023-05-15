from django.db import models
from accounts.models import CustomUser
from pages.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    shipping = models.BooleanField(default=False)

    @property
    def get_cart_total_qty(self):
        order_products = self.orders.all()
        total_qty = sum([product.quantity for product in order_products])
        return total_qty

    @property
    def get_cart_total_price(self):
        order_products = self.orders.all()
        total_qty = sum([product.get_total_price for product in order_products])
        return total_qty


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name="orders")
    quantity = models.IntegerField(default=0, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return self.product.price * self.quantity
