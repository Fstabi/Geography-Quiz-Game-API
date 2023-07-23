from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from core.models import Categories
from categories.serializers import CategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """View for managing categories."""
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
