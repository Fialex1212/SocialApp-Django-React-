from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    #errors

    path('home/', views.home, name='home'),
    path('profile/<int:user_pk>/', views.profile, name='profile'),
]
