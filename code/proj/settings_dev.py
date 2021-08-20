import os

DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = (
    "127.0.0.1",
    "localhost",
)

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "database-postgres-dev",
        "PORT": "5432",
    }
}

USE_CELERY = True
USE_SILK = os.getenv("USE_SILK", False)
LOGGING_CONFIG = None
if os.getenv("DEBUG_CELERY", False):
    CELERY_TASK_ALWAYS_EAGER = True
    CELERY_TASK_EAGER_PROPAGATES = True

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AUTH_PASSWORD_VALIDATORS = []
