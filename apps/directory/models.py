from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AlumniProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="alumni_profile"
    )
    graduation_year = models.PositiveIntegerField()
    major = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    current_job = models.CharField(max_length=100, blank=True)
    current_company = models.CharField(max_length=100, blank=True)
    achievements = models.JSONField(blank=True, default=list)
    skills = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.major} ({self.graduation_year})"

    class Meta:
        indexes = [
            models.Index(fields=["graduation_year"]),
            models.Index(fields=["major"]),
        ]
        verbose_name = "Alumni Profile"
        verbose_name_plural = "Alumni Profiles"
        ordering = [
            "-graduation_year",
            "user__first_name",
            "user__last_name",
        ]  # This is valid for queryset ordering
        unique_together = ("user", "graduation_year", "major")


class AlumniConnection(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("blocked", "Blocked"),
    ]

    requester = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="connection_requests_sent"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="connection_requests_received"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.requester.first_name} -> {self.receiver.first_name} ({self.status})"
        )

    class Meta:
        unique_together = (("requester", "receiver"),)
        indexes = [
            models.Index(fields=["requester", "receiver"]),
            models.Index(fields=["status"]),
        ]
        verbose_name = "Alumni Connection"
        verbose_name_plural = "Alumni Connections"
        ordering = ["-created_at"]
