from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    # path('', views.frontPage, name='front-page'),
    path('', views.profiles, name='profiles'),
    path('saimnieciba/<str:pk>/', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),



    # path('saimniecibas/', views.saimniecibas, name='saimniecibas'),
    # path('saimniecibas/saimnieciba/<str:pk>/',
    #      views.saimnieciba, name='saimnieciba'),

]
