from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from events.models import Event, EventRegistration
from events.serializers import (
    EventSerializer,
    EventListSerializer,
    EventRegistrationSerializer,
)
from apps.users.models import User


class EventViewSet(viewsets.ModelViewSet):
    queryset = (
        Event.objects.all()
        .select_related("organizer")
        .prefetch_related("registrations")
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        return EventSerializer

    def perform_create(self, serializer):
        # Use authenticated user as organizer if not explicitly set
        if not serializer.validated_data.get("organizer"):
            serializer.save(organizer=self.request.user)
        else:
            # If organizer is set manually, check permission
            if serializer.validated_data["organizer"] != self.request.user:
                raise PermissionDenied("You can only create events for yourself.")
            serializer.save()

    def perform_update(self, serializer):
        if serializer.instance.organizer != self.request.user:
            raise PermissionDenied("You can only update your own events.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.organizer != self.request.user:
            raise PermissionDenied("You can only delete your own events.")
        instance.delete()

    @action(detail=True, methods=["get"], url_path="registrations")
    def registrations(self, request, pk=None):
        """Get all registrations for a specific event"""
        event = self.get_object()
        registrations = event.registrations.select_related("user")
        serializer = EventRegistrationSerializer(registrations, many=True)
        return Response(serializer.data)


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all().select_related("event", "user")
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.validated_data["event"]

        # Check for duplicate registration
        if EventRegistration.objects.filter(event=event, user=user).exists():
            raise PermissionDenied("You have already registered for this event.")

        serializer.save(user=user)

    def perform_update(self, serializer):
        registration = serializer.instance
        if registration.user != self.request.user:
            raise PermissionDenied("You can only update your own registration.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You can only cancel your own registration.")
        instance.delete()
