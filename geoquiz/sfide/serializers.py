"""
Serializers for Sfide APIs
"""
from rest_framework import serializers

from core.models import (
    Sfide,
)


class SfideSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Sfide
        fields = [
            'id', 'name', 'difficulty',
        ]
        read_only_fields = ['id']
