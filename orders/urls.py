from django.urls import path, include
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='list'),
    path('<order_id>',  views.order_detail, name='order_detail'),
    path('order/create', views.order_create, name='order_create'),
]
