from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_("Email Address"), unique=True)
    profile = models.ImageField(
        _("Profile"), upload_to="profile/", null=True, blank=True)
    fullname = models.CharField(_("Fullname"), max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()
