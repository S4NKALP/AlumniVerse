import uuid
from django.db import models
from apps.users.models import User

# Create your models here.

EVENT_TYPE_CHOICE = [
    ("networking", "Networking"),
    ("reunion", "Reunion"),
    ("workshop", "Workshop"),
    ("webinar", "Webinar"),
    ("social", "Social"),
    ("career", "Career"),
    ("fundraising", "Fundraising"),
]
EVENT_STATUS_CHOICE = [
    ("draft", "Draft"),
    ("published", "Published"),
    ("cancelled", "Cancelled"),
    ("completed", "Completed"),
]

EVENT_REGISTRATION_STATUS_CHOICE = [
    ("registered", "Registered"),
    ("attended", "Attended"),
    ("cancelled", "Cancelled"),
    ("waitlist", "Waitlist"),
]


class Event(models.Model):
    id = models.AutoField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organized_events"
    )
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_virtual = models.BooleanField(default=False)
    virtual_link = models.URLField(blank=True, null=True)
    max_attendess = models.PositiveIntegerField(blank=True, null=True)
    registration_deadline = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    requires_approval = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to="events/", blank=True, null=True)
    tags = models.JSONFIELD(default=list, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=EVENT_STATUS_CHOICE, default="draft"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "events"
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["start_date"]),
            models.Index(fields=["end_date"]),
            models.Index(fields=["organizer"]),
            models.Index(fields=["status"]),
            models.Index(fields=["event_type"]),
            models.Index(fields=["is_public"]),
            models.Index(fields=["tags"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
            models.Index(fields=["registration_deadline"]),
            models.Index(fields=["location"]),
        ]


class EventRegistration(models.Model):
    id = models.AutoField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_registrations"
    )
    status = models.CharField(
        max_length=50, choices=EVENT_REGISTRATION_STATUS_CHOICE, default="registered"
    )
    registration_date = models.DateTimeField(auto_now_add=True)
    special_requirements = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "event_registrations"
        unique_together = (("event", "user"),)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
