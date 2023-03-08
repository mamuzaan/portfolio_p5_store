from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('wishlist/<int:product_id>/', views.add_product_to_wishlist, name='add_product_to_wishlist'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),
]
