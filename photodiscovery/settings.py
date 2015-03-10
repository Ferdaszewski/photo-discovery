"""
Django settings for photodiscovery project.
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_PATH = os.path.join(BASE_DIR, 'static')
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')


# Secret keys, login, passwords, etc
from photodiscovery.keys import DJANGO_SECRET_KEY, PSQL_ROLE_PASSWORD
SECRET_KEY = DJANGO_SECRET_KEY
DB_PASSWORD = PSQL_ROLE_PASSWORD


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

ROOT_URLCONF = 'photodiscovery.urls'

WSGI_APPLICATION = 'photodiscovery.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'photoappdb',
        'USER': 'photoappdb',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': ''
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
