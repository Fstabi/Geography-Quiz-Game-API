from rest_framework import viewsets
from core.models import Challenges
from .serializers import ChallengesSerializer
from rest_framework.permissions import IsAdminUser


class ChallengesViewSet(viewsets.ModelViewSet):
    queryset = Challenges.objects.all()
    serializer_class = ChallengesSerializer
    permission_classes = [IsAdminUser]
