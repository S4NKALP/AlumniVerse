from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.directory.models import AlumniConnection, AlumniProfile
from apps.directory.serializers import (
    AlumniConnectionSerializer,
    AlumniProfileSerializer,
)


class AlumniProfileViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfile.objects.select_related("user").all()
    serializer_class = AlumniProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlumniConnectionViewSet(viewsets.ModelViewSet):
    queryset = AlumniConnection.objects.select_related("requester", "receiver").all()
    serializer_class = AlumniConnectionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)
