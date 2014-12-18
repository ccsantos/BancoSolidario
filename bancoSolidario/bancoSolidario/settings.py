"""
Django settings for bancoSolidario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from local_settings import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/"
# Redirect when login is not correct.
LOGIN_URL = '/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qqxv0p5ti@ezz@3a#$!#13ay#1gwjflh@4fg%0&t6xa16^#-bj'

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
    'django.contrib.flatpages',
    'django.contrib.sites',
    'django_extensions',
    #'appWeb',
    'crispy_forms',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'bancoSolidario.urls'

WSGI_APPLICATION = 'bancoSolidario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-AR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
     'templates',
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows. 
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(BASE_DIR, 'static'),
    'static',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
CRISPY_TEMPLATE_PACK= 'bootstrap3'
STATIC_URL = '/static/'
