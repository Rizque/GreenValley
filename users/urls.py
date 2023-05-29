from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('select-group/', views.selectGroup, name='select-group'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('edit-farm/', views.editFarm, name='edit-farm'),

    path('farms/', views.farms, name='farms'),
    path('farm/<str:pk>/', views.farm, name='farm'),



    path('', views.frontpage, name='frontpage'),
    path('home/', views.home, name='home'),


]
