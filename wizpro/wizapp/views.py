from rest_framework import viewsets, permissions
from .models import User, Product, OrderProduct, Order, Payment, Address
from .serializers import UserSerializer, ProductSerializer, OrderProductSerializer,\
    OrderSerializer,PaymentSerializer, AddressSerializer
from rest_framework.filters import SearchFilter,OrderingFilter

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name','customer_id')
    permissions_classes =(permissions.IsAuthenticatedOrReadOnly)

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    shirt_count = Product.objects.filter(category='Shirts').count()
    sports_wear_count = Product.objects.filter(category='Sport_Wear').count()
    out_wear_count= Product.objects.filter(category='Out_Wear').count()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('category', 'title')
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

class OrderProductView(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('products', 'ordered_date')
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)


class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('location', 'street_address')
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)


