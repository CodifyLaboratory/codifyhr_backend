from django.shortcuts import get_object_or_404
from rest_framework import views, response, status, viewsets
from rest_framework.response import Response
from .models import Partners
from .serializers import PartnersSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class PartnerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Partners.objects.all()
        serializer = PartnersSerializer(queryset, many=True)
        return Response(serializer.data)