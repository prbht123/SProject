from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
    path('', views.inventory, name='inventory_index'),
    path('create/', views.create, name='inventory_create'),
    path('network/', views.network, name='network_network')
	
]