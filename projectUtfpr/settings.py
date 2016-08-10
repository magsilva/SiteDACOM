"""
Django settings for projectUtfpr project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# configs- Django
# User : root
#Password: root
#email:humberto.g.moreira@gmail.com


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# gettext = lambda s: s
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


ADMINS = (
    # ('humberto', 'humberto_voleibol@hotmail.com'),
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0%&n3=+ir*sbnx8zx7a&4)eic)au3(=ff37!=^zmh0#aebbl-#'

DEBUG = True
# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
# ALLOWED_HOSTS = ['127.0.0.1']



# ALLOWED_HOSTS = []

# Application definition


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'desenvolvimento',
    'haystack',
    'django.contrib.sites',
    'django_extensions',
)



SITE_ID = 1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
ROOT_URLCONF = 'projectUtfpr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'projectUtfpr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'UTFPR',  # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': 'Humberto1!',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.

    },
    'replica': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TESTEUTFPR',
        'USER': 'root',
        'PASSWORD': 'Humberto1!',
        'HOST': '',
        'TEST': {
            'MIRROR': 'default',
            'DEPENDENCY': 'default'
        },
        # ... plus some other settings
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT='/home/humberto/Documentos/projectUtfpr/desenvolvimento/static/'
MEDIA_ROOT='/home/humberto/Documentos/projectUtfpr/desenvolvimento/media/'



HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        'HAYSTACK_SITECONF': 'haystack.search_sites',
    },
}

# if DEBUG:
#     import mimetypes
#     mimetypes.add_type("text/css", ".css", True)
