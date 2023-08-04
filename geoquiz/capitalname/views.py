from rest_framework import viewsets
from challenges.permissions import IsAdminUserOrReadOnly
from core.models import CapitalName
from capitalname.serializers import CapitalNameSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class CapitalNameViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing challenges.
    """
    queryset = CapitalName.objects.all()
    serializer_class = CapitalNameSerializer
    permission_classes = [IsAdminUser, IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication]
