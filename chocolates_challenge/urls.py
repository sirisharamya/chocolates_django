from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('product-list/', views.product_list),
    path('cart/', views.cart),
    path('handle-login/', views.handle_login),
    path('handle-product-list/', views.handle_product_list),
    path('remove-from-cart/', views.remove_from_cart),
    path('handle-cart/', views.handle_cart)
]