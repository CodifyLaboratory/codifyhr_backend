from rest_framework import serializers
from .models import Resume, Wishlist


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ['id',
                  'first_name',
                  'last_name',
                  'surname',
                  'image',
                  'comment',
                  'phone_number',
                  'email',
                  'file',
                  'category',
                  ]


class WishlistSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    wished_resume = ResumeSerializer()


    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']


class WishlistCreateSerializer(serializers.ModelSerializer):

    wished_resume = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']


class WishlistDetailSerializer(serializers.ModelSerializer):

    wished_resume = ResumeSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']


