from pathlib import Path
import os
from django.contrib.messages import constants as messages

"""
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
"""


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "accounts.MedicalWorker"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "debug_toolbar",
    "django_htmx",
    "accounts",
    "cloudinary_storage",
    "cloudinary",
    "externals",
    "patients",
    "laboratory",
    "billing",
    "pharmacy",
    "invetory",
    "doctor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "base.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


if DEBUG == True:
    STATIC_URL = "static/"
    MEDIA_URL = "media/"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "media"),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

    MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")

    INTERNAL_IPS = [
        "127.0.0.1",
    ]

else:
    # ALLOWED_HOSTS = [''] update allowed hosts for production

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "neondb",
            "USER": "tawee.drake",
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": "ep-purple-bonus-60535466.eu-central-1.aws.neon.tech",
            "PORT": "5432",
            "OPTIONS": {"sslmode": "require"},
        }
    }
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": "dnb8rethz",
        "API_KEY": "123456789",
        "API_SECRET": os.environ.get("API_SECRET"),
    }

    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

    STATIC_URL = "https://theetawee.github.io/lifecarefiles/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "redodevs@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}


LOGIN_URL = "login"

SESSION_COOKIE_AGE = 3600
# SESSION_COOKIE_AGE = 12 * 60 * 60  # 12 hours in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     # 'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'formatters': {
#         'django.server': {
#             '()': 'django.utils.log.ServerFormatter',
#             'format': '[{server_time}] {message}',
#             'style': '{',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             #'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         },
#         'django.server': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'django.server',
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             #'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#         },
#         'django.server': {
#             'handlers': ['django.server'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     }
# }


if DEBUG:
    BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/dev")
else:
    BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/prod")


ENTRIES_PER_PAGE = 10