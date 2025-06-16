from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.directory.views import AlumniConnectionViewSet, AlumniProfileViewSet

router = DefaultRouter()
router.register(r"profiles", AlumniProfileViewSet)
router.register(r"connections", AlumniConnectionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
