from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('products', views.Products.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='productDetail'),
]
