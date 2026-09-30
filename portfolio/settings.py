from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production-please')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Vercel sets VERCEL_ENV in its runtime; absent locally and under `manage.py test`.
# Hardening (HTTPS redirect, HSTS, secure cookies) therefore applies only in the
# real deployment — local http://127.0.0.1:8000 keeps working.
ON_VERCEL = bool(os.environ.get('VERCEL_ENV'))
_HARDEN = ON_VERCEL and not DEBUG

SECURE_SSL_REDIRECT = _HARDEN
SECURE_HSTS_SECONDS = 31536000 if _HARDEN else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = _HARDEN
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
CSRF_COOKIE_SECURE = _HARDEN
SESSION_COOKIE_SECURE = _HARDEN

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',          # all Vercel preview URLs
    'martinkiruna.vercel.app',  # your production URL (update this)
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # serves static files on Vercel
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],          # global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'core.context_processors.site_profile',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# No database needed — project data lives in core/data.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
# Django 6 compatible static files storage
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'