from rest_framework import viewsets
from challenges.permissions import IsAdminUserOrReadOnly
from core.models import Challenges
from challenges.serializers import ChallengesSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class ChallengesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing challenges.
    """
    queryset = Challenges.objects.all()
    serializer_class = ChallengesSerializer
    permission_classes = [IsAdminUser, IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication]
