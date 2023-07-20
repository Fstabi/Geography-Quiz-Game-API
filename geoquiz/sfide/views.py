"""
Views for the Sfide APIs
"""
# from drf_spectacular.utils import (extend_schema_view,
# extend_schema, OpenApiParameter,OpenApiTypes,)

from rest_framework import (viewsets,
                            # mixins,
                            # status,
                            )

# from rest_framework.decorators import action
# from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from core.models import (Sfide)

from sfide import serializers


class SfideViewSet(viewsets.ModelViewSet):
    """View for manage Sfide APIs."""
    serializer_class = serializers.SfideSerializer
    queryset = Sfide.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
