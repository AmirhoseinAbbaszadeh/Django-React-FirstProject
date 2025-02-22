"""
URL configuration for backend_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as a_view 
from tasks import views as b_view  

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import TaskViewSet, TaskListCreateView

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from tasks.serializers import UserSerializer 

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('register/', b_view.register, name='register'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
