from rest_framework import viewsets
from core.models import Level
from .serializers import LevelSerializer
from rest_framework.permissions import IsAdminUser


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAdminUser]
