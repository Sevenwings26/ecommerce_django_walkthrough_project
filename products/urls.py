from django.urls import path
from . import views

urlpatterns = [
    path('upload-product/', views.upload_product, name='upload_product'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-update/<int:pk>', views.product_update, name='product_update'),
    path('product-delete/<int:pk>', views.product_delete, name='product_delete'),
               
]
