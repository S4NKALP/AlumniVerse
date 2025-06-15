from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"
    fieldsets = (
        (_("Personal Info"), {"fields": ("avatar", "bio", "location")}),
        (_("Education"), {"fields": ("graduation_year", "degree", "major")}),
        (
            _("Professional Info"),
            {
                "fields": (
                    "current_company",
                    "current_position",
                    "linkedin_url",
                    "website_url",
                )
            },
        ),
        (_("Preferences"), {"fields": ("privacy_level", "notification_preferences")}),
        (
            _("Mentorship"),
            {"fields": ("is_mentor_available", "mentor_skills", "is_job_seeking")},
        ),
    )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_active",
        "is_alumni",
        "is_staff_member",
        "is_admin",
        "last_active",
    )
    list_filter = (
        "is_active",
        "is_alumni",
        "is_staff_member",
        "is_admin",
        "created_at",
        "updated_at",
    )
    search_fields = ("email", "phone", "first_name", "last_name")
    ordering = ("-created_at",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (
            _("Status"),
            {"fields": ("is_active", "is_alumni", "is_staff_member", "is_admin")},
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
        (
            _("Important Dates"),
            {"fields": ("last_login", "created_at", "updated_at", "last_active")},
        ),
    )

    readonly_fields = ("created_at", "updated_at", "last_active")

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )

    inlines = [UserProfileInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "graduation_year",
        "current_company",
        "is_mentor_available",
        "is_job_seeking",
        "privacy_level",
    )
    list_filter = (
        "graduation_year",
        "is_mentor_available",
        "is_job_seeking",
        "privacy_level",
        "created_at",
    )
    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "current_company",
        "degree",
        "major",
    )
    raw_id_fields = ("user",)

    fieldsets = (
        (_("User"), {"fields": ("user",)}),
        (_("Personal Info"), {"fields": ("avatar", "bio", "location")}),
        (_("Education"), {"fields": ("graduation_year", "degree", "major")}),
        (
            _("Professional Info"),
            {
                "fields": (
                    "current_company",
                    "current_position",
                    "linkedin_url",
                    "website_url",
                )
            },
        ),
        (_("Preferences"), {"fields": ("privacy_level", "notification_preferences")}),
        (
            _("Mentorship"),
            {"fields": ("is_mentor_available", "mentor_skills", "is_job_seeking")},
        ),
        (_("Timestamps"), {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user")
