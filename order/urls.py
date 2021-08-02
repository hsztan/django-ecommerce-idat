from django.urls import path
from .views import AddOrderView, CuponListView

urlpatterns = [
    path('cupones', CuponListView.as_view(), name='cupones'),
    path('orders', AddOrderView.as_view(), name='orders')
]
