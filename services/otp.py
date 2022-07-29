from django.conf import settings
from django.utils.crypto import get_random_string
from twilio.rest import Client

from djCRMBackend.dependancies import thread


def send_twilio_sms(msg_to: str, msg_otp: str) -> str:
    client = Client(settings.SMS["account_sid"], settings.SMS["auth_token"])
    message = client.messages.create(
        body=f"Login OTP for The Testing {msg_otp}",
        from_=settings.SMS["from_number"],
        to=f"+91{msg_to}",
    )
    return message