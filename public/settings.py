import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'secret'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'glare',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'public.urls'
WSGI_APPLICATION = 'public.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'glare',
        'USER': 'glare',
        'PASSWORD': 'glare',  # Don't deploy with these creds, people.
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

LOGIN_REDIRECT_URL = "/profile"

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/glass.timeline',
    'https://www.googleapis.com/auth/glass.location',
]

AUTH_EXTRA_ARGUMENTS = {
    "access_type": "offline",
}

from local_settings import *
