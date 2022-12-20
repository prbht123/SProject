from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
    path('', views.inventory, name='inventory_index'),
	path('welcome/', views.welcome, name='inventory_welcome'),
	path('future/', views.future, name='inventory_future')
]