import datetime
# from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
from django.utils.crypto import get_random_string
from django.conf import settings
from django.db import models
from apps.common.models import TimeStampUUIDModel
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import User
# Create your models here.


# User = get_user_model

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


# Customer Model
class Profile(TimeStampUUIDModel):
    user = models.OneToOneField(User, related_name="profiles", on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="profiles/profile_pics", blank=True, verbose_name=_("Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("Zip Code"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"), default="India")
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    is_mobile_verified = models.BooleanField(default=False, verbose_name=_("Mobile verified"))
    is_verified_customer = models.BooleanField(default=False, verbose_name=_("Customer verified"))
    is_admin = models.BooleanField(default=False, verbose_name=_("Admin User"))
    is_manager = models.BooleanField(default=False, verbose_name=_("Store Manager User"))
    is_customer = models.BooleanField(default=False, verbose_name=_("Customer User"))

    @property
    def get_full_name(self):
        return f"{self.user.full_name}"

    @property
    def get_email(self):
        return self.user.email
    
    @property
    def get_mobile(self):
        return self.user.mobile

    @property
    def get_user_uuid(self):
        return self.user.id

    @property
    def get_user_id(self):
        return self.user.pkid

    def __str__(self):
        return f"{self.user.full_name}"

