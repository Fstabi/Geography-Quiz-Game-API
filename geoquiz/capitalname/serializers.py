
from rest_framework import serializers
from core.models import CapitalName


class CapitalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapitalName
        fields = ['id', 'country_name', 'capital_name', 'difficulty']
        read_only_fields = ['id']
