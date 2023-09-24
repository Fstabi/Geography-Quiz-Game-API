from rest_framework import serializers
from core.models import Challenges


class ChallengesSerializer(serializers.ModelSerializer):
    """Serializer for the Challenges model."""

    class Meta:
        model = Challenges
        fields = ['id', 'name', 'difficulty',
                  'level', 'category', 'lat', 'long', 'coordinates' 'photo_link']
        read_only_fields = ['id']
