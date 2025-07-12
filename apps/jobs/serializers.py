from rest_framework import serializers
from jobs.models import Company, JobPosting, JobApplication
from apps.users.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "logo",
            "website",
            "description",
            "industry",
            "size",
            "location",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class JobPostingSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source="company", write_only=True
    )
    posted_by = PosterSerializer(read_only=True)

    class Meta:
        model = JobPosting
        fields = [
            "id",
            "title",
            "company",
            "company_id",
            "posted_by",
            "description",
            "requirements",
            "benefits",
            "location",
            "is_remote",
            "job_type",
            "experience_level",
            "salary_min",
            "salary_max",
            "salary_currency",
            "application_deadline",
            "external_url",
            "skills_required",
            "status",
            "featured",
            "view_count",
            "created_at",
            "updated_at",
            "expires_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "view_count"]


class JobPostingListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = JobPosting
        fields = [
            "id",
            "title",
            "company",
            "location",
            "is_remote",
            "job_type",
            "experience_level",
            "salary_min",
            "salary_max",
            "status",
            "featured",
            "expires_at",
        ]


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class JobApplicationSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)
    applicant_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="applicant", write_only=True, required=False
    )
    job = JobPostingSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=JobPosting.objects.all(), source="job", write_only=True
    )

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "job",
            "job_id",
            "applicant",
            "applicant_id",
            "cover_letter",
            "resume",
            "additional_documents",
            "status",
            "applied_at",
            "last_updated",
        ]
        read_only_fields = ["id", "applied_at", "last_updated", "status"]
