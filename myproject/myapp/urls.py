from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('home/', views.home, name='home'),
    path('profile/<int:pk>/', views.profile, name='profile'),
]