from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "maku-secret-2025"
ALLOWED_HOSTS = ["*"]
DEBUG = True

# URL Configuration
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
MIDDLEWARE = []
DATABASES = {}

# Application definition
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # APPS
    "web",
    "app"
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'
