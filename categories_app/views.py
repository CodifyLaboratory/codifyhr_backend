from django.shortcuts import get_object_or_404
from rest_framework import views, response, status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializers


class CategoriesViewSet(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializers(category)
        return Response(serializer.data)

