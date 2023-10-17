from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='customer-store'),
    path('cart/', views.cart, name='customer-cart'),
    path('checkout/', views.checkout, name='customer-checkout')
]