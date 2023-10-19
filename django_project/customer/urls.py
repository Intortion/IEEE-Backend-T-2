from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name='customer-store'),
    path('cart/', views.cart, name='customer-cart'),
    path('checkout/', views.checkout, name='customer-checkout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)