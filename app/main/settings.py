""" settings.py without all settings that we don't need for project """

# Python improts
from os import getenv
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("SECRET_KEY")
IS_PROD = int(getenv("IS_PROD"))

# if project running on production server
if IS_PROD:
    ALLOWED_HOSTS = [
        "localhost",
        str(getenv("HOST"))
    ]
    DEBUG = False

# if it's running on local machine
else:
    ALLOWED_HOSTS = ['*']
    DEBUG = True

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles", # need for Swagger UI
    "main",
    # app for test task
    "google_drive_api",
    # Swagger
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

STATIC_URL = "static/" # need for django.contrib.staticfiles

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

WSGI_APPLICATION = "main.wsgi.application"

# don't need database for project
DATABASES = {}
# https://stackoverflow.com/a/27086121
REST_FRAMEWORK = {
    # don't that in project
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    # https://www.django-rest-framework.org/api-guide/parsers/#setting-the-parsers
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        ],
     # swagger drf-spectacular
    'DEFAULT_SCHEMA_CLASS': 
        'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERERS': [
        'drf_spectacular.renderers.SpectacularRenderer',
        'rest_framework.renderers.JSONRenderer',
    ]
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(asctime)s %(levelname) -4s %(name) -2s [%(pathname)s:%(lineno)d] %(message)s"},
        "file": {"format": "%(asctime)s %(levelname) -4s %(name) -2s [%(filename)s:%(lineno)d] %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "filename": f"{BASE_DIR}/logs/django_log.log",
            "backupCount": 5,
            "maxBytes": 5242880,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

logger = logging.getLogger(__name__)

# need for Swagger UI
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# Swagger setup
SPECTACULAR_SETTINGS = {
    'TITLE': 'Nova Test Case API',
    'DESCRIPTION': 'Test case for Nova! 🤍',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # https://stackoverflow.com/a/67522312/24040439
    # https://drf-spectacular.readthedocs.io/en/latest/faq.html#filefield-imagefield-is-not-handled-properly-in-the-schema
    "COMPONENT_SPLIT_REQUEST": True
}

