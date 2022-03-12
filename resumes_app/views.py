from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Resume
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ReadOnlyModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']







