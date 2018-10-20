"""
Django settings for prizy project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from distutils.util import strtobool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')mrgma3whkkq8hn!%w+4iw4$1ougvre6_t%@x*hn)hibt+u#=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.getenv('PRIZY_DEBUG_ENABLED', 'True'))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'storages',

    'accounts',
    'events'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prizy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'prizy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

PRIZY_DB_ENGINE = 'django.db.backends.mysql'
PRIZY_DB_NAME = os.getenv('PRIZY_DB_NAME', 'prizy')
PRIZY_DB_USER = os.getenv('PRIZY_DB_USER', 'prizyuser')
PRIZY_DB_PASS = os.getenv('PRIZY_DB_PASSWORD', '')
PRIZY_DB_HOST = os.getenv('PRIZY_DB_HOST', 'localhost')
PRIZY_DB_PORT = os.getenv('PRIZY_DB_PORT', '')

DATABASES = {
    'default': {
        'ENGINE': PRIZY_DB_ENGINE,
        'NAME': PRIZY_DB_NAME,
        'USER': PRIZY_DB_USER,
        'PASSWORD': PRIZY_DB_PASS,
        'HOST': PRIZY_DB_HOST,
        'PORT': PRIZY_DB_PORT,
    }
}


# REST Framework Authentication configuration
# Primary default authentication method is JWT

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "accounts.Account"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# JWT Auth configuration
# Allow JWT refresh upon expiry

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': os.getenv('JWT_EXPIRATION_DELTA', datetime.timedelta(days=1)),
    'JWT_ALLOW_REFRESH': os.getenv('JWT_ALLOW_REFRESH', 'True')
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
