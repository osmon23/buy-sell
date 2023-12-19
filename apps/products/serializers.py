from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.CharField(default=None)

    class Meta:
        model = Category
        fields = (
            'name',
            'parent',
        )
        read_only_fields = (
            'id',
        )
