from django.urls import path
from . import views
urlpatterns = [
    path('', views.products, name='products'),
    path('produkts/<str:pk>/', views.product, name='product'),
    path('pievienot-produktu/', views.createProduct, name='create-product'),
    path('rediget-produktu/<str:pk>/',
         views.updateProduct, name='update-product'),
    path('dzest-produktu/<str:pk>/', views.deleteProduct, name='delete-product'),

]
