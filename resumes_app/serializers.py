from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ['id',
                  'first_name',
                  'last_name',
                  'surname',
                  'image',
                  'comment',
                  'link',
                  'category',
                  ]

