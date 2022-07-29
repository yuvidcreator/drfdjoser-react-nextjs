from djCRMBackend.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         "ENGINE": env("DEV_DB_ENGINE"),
#         "NAME": env("DEV_DB_NAME"),
#         "USER": env("DEV_DB_USER"),
#         "PASSWORD": env("DEV_DB_PASS"),
#         "HOST": env("DEV_DB_HOST"),
#         "PORT": env("DEV_DB_PORT"),
#     }
# }

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": env("DEV_DB_ENGINE"),
            "NAME": env("DEV_DB_NAME"),
            "USER": env("DEV_DB_USER"),
            "PASSWORD": env("DEV_DB_PASS"),
            "HOST": env("DEV_DB_HOST"),
            "PORT": env("DEV_DB_PORT"),
        }
    }