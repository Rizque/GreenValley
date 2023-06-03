from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<uuid:category_id>/',
         views.category_products, name='category_products'),

    path('product/<str:pk>/', views.product, name='product'),
    path('rate/<uuid:product_id>/<int:rating>/', views.rate),

    path('add-product/', views.createProduct, name='add-product'),
    path('update-product/<str:pk>/',
         views.updateProduct, name='update-product'),
    path('delete-product/<str:pk>/', views.deleteProduct, name='delete-product'),

]
