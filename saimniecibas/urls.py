from django.urls import path
from . import views

urlpatterns = [
    path('', views.sakumlapa, name='sakumlapa'),
    path('saimniecibas/', views.saimniecibas, name='saimniecibas')
]
