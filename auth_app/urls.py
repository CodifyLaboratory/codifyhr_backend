from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns  = [
    path('user/<int:pk>/', PersonalRoomViewSet.as_view({'get': 'retrieve'})),
    path('login/', obtain_auth_token, name='user-obtain_auth_token'),
]
