from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
    path('', views.inventory, name='inventory_index'),
    path('create/', views.create, name='inventory_create'),
    path('contact/', views.contact, name='contact_contact'),
    path('system/', views.system, name='system_system')
	
]