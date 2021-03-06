"""
Django settings for gamesapi project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hqxo-nbu)en!sv73ing#0(za9f8dizy29e1*q1p%9s^44#bu=$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '127.0.0.1', '192.168.0.102','192.168.0.103','192.168.0.104','192.168.0.105','192.168.0.106','192.168.0.107','192.168.0.108','192.168.0.109','192.168.0.110','192.168.0.111','192.168.0.112','192.168.0.113','192.168.0.114','192.168.0.115','192.168.0.116','192.168.0.117','192.168.0.118','192.168.0.119','192.168.0.120','192.168.0.121','192.168.0.122','192.168.0.123','192.168.0.124','192.168.0.125','192.168.0.126','192.168.0.127','192.168.0.128','192.168.0.129','192.168.0.130','192.168.0.131','192.168.0.132','192.168.0.133','192.168.0.134','192.168.0.135','192.168.0.136','192.168.0.137','192.168.0.138','192.168.0.139','192.168.0.140','192.168.0.141','192.168.0.142','192.168.0.143','192.168.0.144','192.168.0.145','192.168.0.146','192.168.0.147','192.168.0.148','192.168.0.149','192.168.0.150','192.168.0.151','192.168.0.152','192.168.0.153','192.168.0.154','192.168.0.155','192.168.0.156','192.168.0.157','192.168.0.158','192.168.0.159','192.168.0.160','192.168.0.161','192.168.0.162','192.168.0.163','192.168.0.164','192.168.0.165','192.168.0.166','192.168.0.167','192.168.0.168','192.168.0.169','192.168.0.170','192.168.0.171','192.168.0.172','192.168.0.173','192.168.0.174','192.168.0.175','192.168.0.176','192.168.0.177','192.168.0.178','192.168.0.179','192.168.0.180','192.168.0.181','192.168.0.182','192.168.0.183','192.168.0.184','192.168.0.185','192.168.0.186','192.168.0.187','192.168.0.188','192.168.0.189','192.168.0.190','192.168.0.191','192.168.0.192','192.168.0.193','192.168.0.194','192.168.0.195','192.168.0.196','192.168.0.197','192.168.0.198','192.168.0.199','192.168.0.200','192.168.0.201','192.168.0.202','192.168.0.203','192.168.0.204','192.168.0.205','192.168.0.206'  ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'games.apps.GamesConfig',
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

ROOT_URLCONF = 'gamesapi.urls'

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

WSGI_APPLICATION = 'gamesapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
