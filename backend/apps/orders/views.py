from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from ..user.mixins import CustomLoginRequiredMixin
from . models import Order, OrderItem
from apps.carts.models import Cart
from . serializers import OrderSerializer
from . forms import OrderForm, OrderItemForm

# Create your views here.
class OrderAdd (CustomLoginRequiredMixin, generics.CreateAPIView) :
    queryset = Order.objects.all ()
    serializer_class = OrderSerializer

    def get (self, request, *args, **kwargs) :
        self.queryset = Cart.objects.order_by ("-created_at").filter(user = request.login_user)
        return self.list (request, *args, **kwargs)