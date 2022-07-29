from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _



class CustomUserManager(BaseUserManager):
    
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Must provide a valid Email Address'))

    def create_user(self, email, mobile, first_name, last_name, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email).lower()
            self.email_validator(email)
        else:
            raise ValueError(_('Active & Valid Email is mandatory'))

        if not mobile:
            raise ValueError(_('You must Provide a valid Mobile No.'))

        if not first_name:
            raise ValueError(_('You must submit your First Name'))

        if not last_name:
            raise ValueError(_('You must submit your Last Name'))

        user = self.model(
            email=email,
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
            full_name=first_name+" "+last_name,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, first_name, last_name, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if not password:
            raise ValueError(_("Superuser must have a Password"))

        if email:
            email = self.normalize_email(email).lower()
            self.email_validator(email)
        else:
            raise ValueError(_('Active Email is mandatory'))

        user = self.create_user(email, mobile, first_name, last_name, password, **extra_fields)
        user.save(using=self._db)
        return user