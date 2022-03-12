from rest_framework import serializers
from .models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]

    def validate(self, data):
        data = super().validate(data)
        name = data['name']
        if not name:
            raise serializers.ValidationError('This field required')

        queryset = Category.objects.all()
        for instance in queryset:
            if instance.name == name:
                raise serializers.ValidationError(detail="Такая категория уже существует", code="Категория создана")

        return data

