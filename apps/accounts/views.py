from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from apps.accounts.models import UserProfile
from apps.accounts.serializers import UserSerializer, UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(
        detail=False,
        methods=["get"],
        url_path="me",
        permission_classes=[permissions.IsAuthenticated],
    )
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.select_related("user").all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=False,
        methods=["get"],
        url_path="me",
        permission_classes=[permissions.IsAuthenticated],
    )
    def my_profile(self, request):
        profile = request.user.profile
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
