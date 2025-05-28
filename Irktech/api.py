from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from Irktech.models import Order, Vent, List, Client
from Irktech.serializers import OrderSerializer, ListSerializer, VentSerializer, ClientSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        # Получаем или создаем клиента
        client, created = Client.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'client_id': client.id
        })

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
