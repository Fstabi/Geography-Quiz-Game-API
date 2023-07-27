from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from challenges.permissions import IsAdminUserOrReadOnly
from core.models import Challenges
from challenges.serializers import ChallengesSerializer


class ChallengesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing challenges.
    """
    queryset = Challenges.objects.all()
    serializer_class = ChallengesSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
