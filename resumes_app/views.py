from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Resume, Wishlist
from .serializers import ResumeSerializer, WishlistDetailSerializer, WishlistSerializer, WishlistCreateSerializer


class ResumeReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class WishlistModelViewSet(ModelViewSet):
    """ Закладки """

    def perform_create(self, serializer):
        try:
            wished_resume = Resume.objects.get(id=self.kwargs['pk'])
            return serializer.save(user=self.request.user, wished_resume=wished_resume)
        except:
            raise NotFound

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Wishlist.objects.filter(user_id=self.request.user.id)
        elif self.action == 'post' or self.action == 'destroy':
            return Wishlist.objects.all()

    def get_serializer_class(self):
        try:
            if self.action == 'list':
                return WishlistSerializer
            if self.action == 'create':
                return WishlistCreateSerializer
            elif self.action == 'destroy':
                return WishlistDetailSerializer
            else:
                return WishlistSerializer
        except:
            raise AuthenticationFailed
