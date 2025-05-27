from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from Irktech.models import Order, Vent, List, Client
from Irktech.serializers import OrderSerializer, ListSerializer, VentSerializer, ClientSerializer

class OrdersViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ListsViewset(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer

class VentsViewset(
    mixins.ListModelMixin,
    GenericViewSet):

    queryset = Vent.objects.all()
    serializer_class = VentSerializer

class ClientsViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
