from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

    def validate(self, data):
        data = super().validate(data)
        name = data['name']
        if not name:
            raise serializers.ValidationError('This field required')

        for instance in Category.objects.all():
            if instance.name == name:
                raise serializers.ValidationError(detail="Такая категория уже существует", code="Категория создана")

        return data


class ReturnNameSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return value.name


class ResumeSerializer(serializers.ModelSerializer):

    category = ReturnNameSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ['id',
                  'first_name',
                  'last_name',
                  'surname',
                  'comment',
                  'phone_number',
                  'email',
                  'file',
                  'category',
                  ]


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['id', 'title', 'link','image']


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
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    wished_resume = ResumeSerializer()

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']