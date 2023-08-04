from rest_framework import viewsets
from core.models import Level
from rest_framework.authentication import TokenAuthentication
from .serializers import LevelSerializer
from rest_framework.permissions import IsAdminUser


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
