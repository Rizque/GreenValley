from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('select-group/', views.selectGroup, name='select-group'),
    path('profile/', views.profile, name='profile'),

    path('', views.frontpage, name='frontpage'),
    path('home/', views.home, name='home'),


]
