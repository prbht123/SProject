from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
    path('', views.inventory, name='inventory_index'),
    path('training/', views.training, name='inventory_training')

	
]