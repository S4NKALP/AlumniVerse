from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.directory.models import AlumniConnection, AlumniProfile


@admin.register(AlumniProfile)
class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_email",
        "graduation_year",
        "major",
        "degree",
        "current_company",
        "current_job",
    )
    list_filter = (
        "graduation_year",
        "major",
        "degree",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "major",
        "degree",
        "current_company",
        "current_job",
        "skills",
    )
    raw_id_fields = ("user",)

    fieldsets = (
        (_("User Information"), {"fields": ("user",)}),
        (_("Academic Information"), {"fields": ("graduation_year", "major", "degree")}),
        (_("Professional Information"), {"fields": ("current_job", "current_company")}),
        (_("Skills & Achievements"), {"fields": ("skills", "achievements")}),
        (
            _("Timestamps"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    readonly_fields = ("created_at", "updated_at")

    @admin.display(description="User Email")
    def user_email(self, obj):
        return getattr(obj.user, "email", "-")


@admin.register(AlumniConnection)
class AlumniConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "requester_email",
        "receiver_email",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "requester__email",
        "requester__first_name",
        "requester__last_name",
        "receiver__email",
        "receiver__first_name",
        "receiver__last_name",
        "message",
    )
    raw_id_fields = ("requester", "receiver")

    fieldsets = (
        (_("Connection Details"), {"fields": ("requester", "receiver", "status")}),
        (_("Additional Information"), {"fields": ("message",)}),
        (
            _("Timestamps"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    readonly_fields = ("created_at", "updated_at")

    @admin.display(description="Requester Email")
    def requester_email(self, obj):
        return getattr(obj.requester, "email", "-")

    @admin.display(description="Receiver Email")
    def receiver_email(self, obj):
        return getattr(obj.receiver, "email", "-")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("requester", "receiver")
