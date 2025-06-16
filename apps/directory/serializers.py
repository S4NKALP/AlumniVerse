from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.directory.models import AlumniConnection, AlumniProfile

User = get_user_model()


class AlumniProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True
    )  # or use PrimaryKeyRelatedField

    class Meta:
        model = AlumniProfile
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class AlumniConnectionSerializer(serializers.ModelSerializer):
    requester = serializers.StringRelatedField(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = AlumniConnection
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "status")
