from django.urls import path
from .views import OrderCreateListView, CuponListView

urlpatterns = [
    path('cupones', CuponListView.as_view(), name='cupones'),
    path('orders', OrderCreateListView.as_view(), name='orders')
]
