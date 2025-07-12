from rest_framework.routers import DefaultRouter
from jobs.views import CompanyViewSet, JobPostingViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r"companies", CompanyViewSet)
router.register(r"jobs", JobPostingViewSet)
router.register(r"applications", JobApplicationViewSet)

urlpatterns = router.urls
