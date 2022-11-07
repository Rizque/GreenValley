from django.urls import path
from . import views
urlpatterns = [
    path('', views.produkcija, name='produkcija'),
    path('produkts/<str:pk>/', views.produkts, name='produkts'),
]
