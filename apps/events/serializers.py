from events.models import (
    Event,
    EventRegistration,
)
from rest_framework import serializers

from apps.users.models import User


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class EventRegistrationSerializer(serializers.ModelSerializer):
    user = OrganizerSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = EventRegistration
        fields = [
            "id",
            "event",
            "user",
            "user_id",
            "status",
            "registration_date",
            "special_requirements",
        ]
        read_only_fields = ("id", "registration_date")


class EventSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer(read_only=True)
    organizer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="organizer", write_only=True
    )
    registrations = EventRegistrationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "organizer",
            "organizer_id",
            "event_type",
            "start_date",
            "end_date",
            "location",
            "is_virtual",
            "virtual_link",
            "max_attendess",
            "registration_deadline",
            "is_public",
            "requires_approval",
            "featured_image",
            "tags",
            "status",
            "created_at",
            "updated_at",
            "registrations",
        ]
        read_only_fields = ("id", "created_at", "updated_at")


# Optional: for event listing only
class EventListSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "event_type",
            "start_date",
            "end_date",
            "location",
            "is_virtual",
            "status",
            "organizer",
        ]
