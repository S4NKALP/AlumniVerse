from django.db import models

# Create your models here.

APPROVAL_STATUS_CHOICE = [
    ("draft", "Draft"),
    ("pending", "Pending Review"),
    ("active", "Active"),
    ("closed", "Closed"),
    ("rejected", "Rejected"),
]
EXPERIENCE_LEVEL_CHOICES = [
    ("entry", "Entry Level"),
    ("mid", "Mid Level"),
    ("senior", "Senior Level"),
    ("executive", "Executive"),
]

JOB_TYPE_CHOICES = [
    ("full_time", "Full Time"),
    ("part_time", "Part Time"),
    ("contract", "Contract"),
    ("internship", "Internship"),
    ("freelance", "Freelance"),
]

JOB_APPLICATION_STATUS = [
    ("submitted", "Submitted"),
    ("under_review", "Under Review"),
    ("shortlisted", "Shortlisted"),
    ("interview", "Interview"),
    ("offered", "Offered"),
    ("hired", "Hired"),
    ("rejected", "Rejected"),
    ("withdrawn", "Withdrawn"),
]


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="companies/", null=True, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.name


class JobPosting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_postings"
    )
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posted_jobs"
    )
    description = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    is_remote = models.BooleanField(default=False)
    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
    )
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    salary_currency = models.CharField(max_length=3, default="USD")
    application_deadline = models.DateTimeField(null=True, blank=True)
    external_url = models.URLField(blank=True)
    skills_required = models.JSONField(default=list)
    status = models.CharField(
        max_length=20,
        choices=APPROVAL_STATUS_CHOICE,
        default="pending",
    )
    featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["company"]),
            models.Index(fields=["status"]),
        ]


class JobApplication(models.Model):
    job = models.ForeignKey(
        JobPosting, on_delete=models.CASCADE, related_name="applications"
    )
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_applications"
    )
    cover_letter = models.TextField()
    resume = models.FileField(upload_to="resumes/")
    additional_documents = models.JSONField(default=list)
    status = models.CharField(
        max_length=20,
        choices=JOB_APPLICATION_STATUS,
        default="submitted",
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["job", "applicant"]
