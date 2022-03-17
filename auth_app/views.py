from rest_framework import views, response, status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.admin import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny, IsAuthenticated


class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalRoomViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(pk=self.request.user.id)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)