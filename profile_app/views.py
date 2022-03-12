from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer, WishlistDetailSerializer


class WishlistViewSet(viewsets.ModelViewSet):

    queryset = Wishlist.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return WishlistSerializer
        return WishlistDetailSerializer
