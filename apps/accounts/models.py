import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models, IntegrityError
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, phone=None, password=None, **extra_fields):
        if not email and not phone:
            raise ValueError("User must have an email or a phone number.")

        if email:
            email = self.normalize_email(email)

        try:
            user = self.model(email=email, phone=phone, **extra_fields)

            if not password:
                raise ValueError("Password must be provided.")
            user.set_password(password)
            user.save(using=self._db)
            return user

        except IntegrityError as e:
            # Handle unique constraints more clearly
            if "unique" in str(e).lower():
                if email and self.model.objects.filter(email=email).exists():
                    raise ValueError("A user with this email already exists.")
                if phone and self.model.objects.filter(phone=phone).exists():
                    raise ValueError("A user with this phone number already exists.")
            raise

    def create_superuser(self, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_active", True)

        if not password:
            raise ValueError("Superuser must have a password.")
        if not email:
            raise ValueError("Superuser must have an email address.")

        return self.create_user(
            email=email, phone=phone, password=password, **extra_fields
        )


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",
                message="Phone number must be 10 digits.",
            )
        ],
    )

    is_active = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=True)
    is_staff_member = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_active = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        indexes = [
            models.Index(fields=["email"], name="user_email_idx"),
            models.Index(fields=["phone"], name="user_phone_idx"),
            models.Index(fields=["first_name", "last_name"], name="user_name_idx"),
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)

    graduation_year = models.PositiveIntegerField(null=True, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=100, blank=True)

    current_company = models.CharField(max_length=100, blank=True)
    current_position = models.CharField(max_length=100, blank=True)

    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    privacy_level = models.CharField(
        max_length=20,
        choices=[
            ("public", "Public"),
            ("alumni_only", "Alumni Only"),
            ("private", "Private"),
        ],
        default="alumni_only",
    )

    notification_preferences = models.JSONField(default=dict)
    is_mentor_available = models.BooleanField(default=False)
    mentor_skills = models.JSONField(default=list)
    is_job_seeking = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Profile"

    class Meta:
        indexes = [
            models.Index(fields=["graduation_year"], name="profile_grad_year_idx"),
            models.Index(fields=["current_company"], name="profile_company_idx"),
            models.Index(fields=["is_mentor_available"], name="profile_mentor_idx"),
            models.Index(fields=["is_job_seeking"], name="profile_jobseek_idx"),
        ]
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
