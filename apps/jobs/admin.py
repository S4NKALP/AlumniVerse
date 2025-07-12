from django.contrib import admin
from jobs.models import Company, JobPosting, JobApplication


class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0
    readonly_fields = ("applicant", "status", "applied_at", "last_updated")
    can_delete = False


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "industry", "size", "location", "created_at")
    search_fields = ("name", "industry", "location")
    list_filter = ("industry", "size", "location")
    readonly_fields = ("created_at",)


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "posted_by",
        "job_type",
        "experience_level",
        "location",
        "is_remote",
        "status",
        "featured",
        "view_count",
        "application_deadline",
        "created_at",
    )
    list_filter = (
        "job_type",
        "experience_level",
        "status",
        "featured",
        "is_remote",
        "created_at",
        "application_deadline",
        "expires_at",
    )
    search_fields = (
        "title",
        "company__name",
        "location",
        "skills_required",
        "posted_by__username",
    )
    date_hierarchy = "created_at"
    autocomplete_fields = ("company", "posted_by")
    inlines = [JobApplicationInline]
    readonly_fields = ("view_count", "created_at", "updated_at")

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "title",
                    "company",
                    "posted_by",
                    "description",
                    "requirements",
                    "benefits",
                    "skills_required",
                )
            },
        ),
        (
            "Job Details",
            {
                "fields": (
                    "job_type",
                    "experience_level",
                    "location",
                    "is_remote",
                    "salary_min",
                    "salary_max",
                    "salary_currency",
                )
            },
        ),
        (
            "Status & Metadata",
            {
                "fields": (
                    "status",
                    "featured",
                    "view_count",
                    "application_deadline",
                    "expires_at",
                    "external_url",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "job",
        "applicant",
        "status",
        "applied_at",
        "last_updated",
    )
    list_filter = ("status", "applied_at", "last_updated")
    search_fields = ("job__title", "applicant__username")
    autocomplete_fields = ("job", "applicant")
    readonly_fields = ("applied_at", "last_updated")
