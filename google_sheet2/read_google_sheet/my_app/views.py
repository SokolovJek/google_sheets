from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Orders
from .serializers import OrdersModelSerializer


class OrdersModelViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersModelSerializer
