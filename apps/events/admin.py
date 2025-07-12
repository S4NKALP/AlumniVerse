from django.contrib import admin
from events.models import Event, EventRegistration


class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0
    readonly_fields = ("user", "status", "registration_date")
    can_delete = False


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "event_type",
        "organizer",
        "start_date",
        "end_date",
        "status",
        "is_virtual",
        "is_public",
        "requires_approval",
    )
    list_filter = (
        "event_type",
        "status",
        "is_virtual",
        "is_public",
        "requires_approval",
        "start_date",
        "end_date",
        "registration_deadline",
    )
    search_fields = ("title", "description", "location", "organizer__username")
    date_hierarchy = "start_date"
    inlines = [EventRegistrationInline]
    autocomplete_fields = ["organizer"]
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "title",
                    "description",
                    "event_type",
                    "organizer",
                    "tags",
                )
            },
        ),
        (
            "Schedule & Location",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "location",
                    "is_virtual",
                    "virtual_link",
                )
            },
        ),
        (
            "Registration & Access",
            {
                "fields": (
                    "max_attendess",
                    "registration_deadline",
                    "is_public",
                    "requires_approval",
                )
            },
        ),
        (
            "Status & Media",
            {
                "fields": (
                    "status",
                    "featured_image",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "event",
        "user",
        "status",
        "registration_date",
    )
    list_filter = ("status", "registration_date", "event")
    search_fields = ("event__title", "user__username")
    autocomplete_fields = ["event", "user"]
    readonly_fields = ("registration_date",)
