from xmlrpc.client import FastMarshaller
from django.db import models
from apps.items.models import Item
from apps.user.models import User
from config.constants import *

# Create your models here.
class Order (models.Model) :
    class Meta (object) :
        db_table = "order"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default="anonymous"
    )
    total_price = models.DecimalField(
        "Total Price", blank=False, null=False, max_digits=14, decimal_places=2
    )
    full_name=models.CharField(
        "Full Name", blank=False, null=False, max_length=20, db_index=True, default="Anonymous"
    )
    address_line1 = models.CharField (
        "Address Line 1", blank=False, null=False, max_length=60, db_index=True, default="Anonymous"
    )
    address_line2 = models.CharField (
        "Address Line 2", blank=False, null=False, max_length=60, db_index=True, default="Anonymous"
    )
    city = models.CharField(
        "City", blank=False, null=False, max_length=20, db_index=True
    )
    state= models.CharField(
        "State", blank=False, null=False, max_length=20, db_index=True
    )
    postal_code = models.IntegerField(
        "Postal Code", blank=False, db_index=True
    )
    country = models.CharField(
        "Country", blank=False, null=False, max_length=20, db_index=True
    )
    telephone = models.IntegerField(
        "Telephone", blank=False, db_index=True
    )
    created_at = models.DateTimeField (
        "Created Datetime", blank=True, null=True, auto_now_add=True
    )
    updated_at = models.DateTimeField (
        "Updated Datetime", blank=True, null=True, auto_now=True
    )

class OrderItem (models.Model) :
    class Meta (object) :
        db_table = "order item"
        
    order_id = models.IntegerField(
        "Order ID", blank=False, db_index=True
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        "Quantity", blank=False, db_index=True
    )
    created_at = models.DateTimeField (
        "Created Datetime", blank=True, null=True, auto_now_add=True
    )
    updated_at = models.DateTimeField (
        "Updated Datetime", blank=True, null=True, auto_now=True
    )