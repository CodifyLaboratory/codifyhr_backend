from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('login/', obtain_auth_token, name='user-obtain_auth_token'),
]
