from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.accounts.models import UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["id", "created_at", "updated_at"]  # optional
        read_only_fields = ["user"]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "email", "phone",
            "is_active", "is_alumni", "is_staff_member", "is_admin",
            "created_at", "updated_at", "last_active", "password", "profile"
        ]
        read_only_fields = [
            "id", "is_active", "is_alumni", "is_staff_member", "is_admin",
            "created_at", "updated_at", "last_active", "profile"
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
