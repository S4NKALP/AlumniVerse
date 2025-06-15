from rest_framework.routers import DefaultRouter
from apps.accounts.views import UserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"profiles", UserProfileViewSet)

urlpatterns = [
    *router.urls,
]
