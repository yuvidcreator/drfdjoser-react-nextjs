import datetime
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers import CustomUserManager
# Create your models here.






class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = None
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    mobile = models.IntegerField(verbose_name=_("Mobile No"), unique=True, null=True, blank=True,)
    full_name = models.CharField(max_length=50, blank=True, verbose_name=_("Full Name"))
    first_name = models.CharField(max_length=64, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=64, blank=True, verbose_name=_("Last Name"))
    date_joined = models.DateTimeField(default=timezone.now, verbose_name=_("Registered On"))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated On"))

    # profiles flags
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile", "first_name", "last_name"]
    
    objects = CustomUserManager()

    class Meta:
        verbose_name=_("User")
        verbose_name_plural=_("Users")
        db_table = "users"  # Table Name

    @property
    def get_full_name(self):
        return f"{self.full_name}"

    def _str_(self):
        return f"{self.full_name}"


