from django.urls import path
from . import views
from .views import SaimniecibasListView, SaimniecibaDetailView, SaimniecibaUpdateView, redigetProfilu

urlpatterns = [
    path('', views.sakumlapa, name='sakumlapa'),
    path('saimniecibas/', SaimniecibasListView.as_view(), name='saimniecibas'),
    path('saimniecibas/saimnieciba/<str:pk>/',
         SaimniecibaDetailView.as_view(), name='saimnieciba'),
    path('saimniecibas/saimnieciba/<str:pk>/rediget/',
         SaimniecibaUpdateView.as_view(), name='saimnieciba-rediget'),
    path('profils/', views.lietotajaProfils, name='profils'),
    path('rediget-profilu/', views.redigetProfilu, name='rediget-profilu'),



]
