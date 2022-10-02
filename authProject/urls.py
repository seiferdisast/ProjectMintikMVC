"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from authApp.views.patientsView import PatientsView
from authApp.views.usersList import UsersList

from authApp.views.actualyzationView import UpdateUserView
from authApp.views.userDeleteView import UserDeleteView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()), #deprecated
    path('patients/', PatientsView.as_view()), #deprecated
    path('users/', UsersList.as_view()),
    path('user/<int:pk>/update/', UpdateUserView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view()),
]