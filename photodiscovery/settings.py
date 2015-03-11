"""
Django settings for photodiscovery project.
"""
from django.core.exceptions import ImproperlyConfigured
import json


# Project paths and directories
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_PATH = os.path.join(BASE_DIR, 'static')
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (TEMPLATE_PATH,)


# JSON based secrets module
with open(BASE_DIR + '/photodiscovery/secrets.json', 'r') as f:
    SECRETS = json.load(f)


def get_secret(setting, secrets=SECRETS):
    """Helper function to get a secret with a key of 'setting'."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# Django Secret key, change before production
SECRET_KEY = get_secret('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'visualize',
    'registration',
    'imagekit',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


#
ROOT_URLCONF = 'photodiscovery.urls'

WSGI_APPLICATION = 'photodiscovery.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'photoappdb',
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': get_secret('DB_HOST'),
        'PORT': get_secret('DB_PORT')
    }
}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
    )


# Media files (user upload)
MEDIA_URL = '/media/'


# Registration settings
LOGIN_URL = '/accounts/login/'
REGISTRATION_OPEN = True
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'
