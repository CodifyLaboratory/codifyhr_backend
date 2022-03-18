from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns  = [
    path('login/', obtain_auth_token, name='user-obtain_auth_token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', PersonalRoomViewSet.as_view({'get': 'retrieve'})),
]
