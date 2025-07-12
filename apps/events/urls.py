from rest_framework.routers import DefaultRouter
from events.views import EventViewSet, EventRegistrationViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"registrations", EventRegistrationViewSet)

urlpatterns = [
    *router.urls,
]
