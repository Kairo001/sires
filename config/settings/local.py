import os

from dotenv import load_dotenv
from .base import *

# Load environment variables from .env file
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

# SECURITY WARNING: keep the secret key used in production secret!\
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
