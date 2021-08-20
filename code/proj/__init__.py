import os
from .celery import app as celery_app

__all__ = ["celery_app"]

__version__ = os.getenv("APP_VERSION", "latest")
VERSION = __version__

__staging_code_version__ = __version__
