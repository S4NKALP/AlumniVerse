from jobs.models import Company, JobApplication, JobPosting
from jobs.serializers import (
    CompanySerializer,
    JobApplicationSerializer,
    JobPostingListSerializer,
    JobPostingSerializer,
)
from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all().select_related("company", "posted_by")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return JobPostingListSerializer
        return JobPostingSerializer

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.posted_by != self.request.user:
            raise PermissionDenied("You can only update jobs you've posted.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.posted_by != self.request.user:
            raise PermissionDenied("You can only delete jobs you've posted.")
        instance.delete()


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.select_related("job", "applicant").all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        job = serializer.validated_data["job"]
        applicant = self.request.user

        if JobApplication.objects.filter(job=job, applicant=applicant).exists():
            raise PermissionDenied("You have already applied for this job.")

        serializer.save(applicant=applicant)

    def perform_update(self, serializer):
        if serializer.instance.applicant != self.request.user:
            raise PermissionDenied("You can only modify your own applications.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.applicant != self.request.user:
            raise PermissionDenied("You can only delete your own applications.")
        instance.delete()
