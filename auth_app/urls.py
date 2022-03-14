from django.urls import path
from .views import UserRegisterAPIViews
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token, name='user-obtain_auth_token'),
    path('register/', obtain_auth_token, name='user-obtain_auth_token'),
    path('logout/', obtain_auth_token, name='user-obtain_auth_token'),
]
