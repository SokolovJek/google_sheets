from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Orders


class OrdersModelSerializer(HyperlinkedModelSerializer):


    class Meta:
        model = Orders
        fields = '__all__'
