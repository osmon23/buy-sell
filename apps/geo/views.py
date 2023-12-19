from rest_framework import viewsets, permissions

from .models import Geo
from .serializers import GeoSerializer


class GeoViewSet(viewsets.ModelViewSet):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    permission_classes = [permissions.AllowAny]
