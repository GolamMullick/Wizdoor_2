from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register('users', views.UserView, base_name='users')
router.register('products', views.ProductView, base_name='products')
router.register('order_products', views.OrderProductView, base_name='order_products')
router.register('order', views.OrderView, base_name='orders')
router.register('payment', views.PaymentView, base_name='payment')
router.register('address', views.AddressView, base_name='address')


urlpatterns = [
   path('', include(router.urls)),

]