import re
from django.db.models import Q
from apps.accounts.models import User


def password_validation(password: str):
    """ ### password validation """
    if len(password) < 8:
        return "Password must be more than 8 chanracter"
    elif not re.search("[a-z]", password):
        return "Password must have atleast one letter"
    elif not re.search("[1-9]", password):
        return "Password must have atleast one number"
    elif not re.search("[~!@#$%^&*]", password):
        return "Password must have atleast one special character"
    elif re.search("[\s]", password):
        return "Space must not be there"
    else:
        return True


def authenticate_user(request, email_or_mobile: str, password: str) -> str:
    error_msg = "Invalid Credentials"
    pwd_error_msg = "Password is incorrect "
    no_user_error_msg = "User not found "
    user = User.objects.filter(
        Q(email=email_or_mobile) | Q(mobile=email_or_mobile)
    ).first()
    if not user:
        return False, no_user_error_msg
    if "@" not in email_or_mobile:
        if not user.is_mobile_verified:
            return False, "Mobile number is not verified"
    if user:
        if user.check_password(password):
            return user, None
        else:
            return False, pwd_error_msg
    return False, error_msg