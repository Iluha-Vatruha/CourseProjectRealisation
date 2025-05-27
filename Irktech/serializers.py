from rest_framework import serializers

from Irktech.models import Order, List, Vent, Client



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'orderNumber', 'user', 'comment', 'date']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'orderNumber', 'ventName', 'param', 'quantity']

class VentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vent
        fields = ['id', 'ventName', 'picture']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'name', 'email', 'phone' ]