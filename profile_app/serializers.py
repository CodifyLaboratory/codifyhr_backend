from rest_framework import serializers
from .models import Wishlist
from resumes_app.serializers import ResumeSerializer

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']


class WishlistDetailSerializer(serializers.ModelSerializer):

    wished_resume = ResumeSerializer()

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']

