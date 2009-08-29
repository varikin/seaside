# Django settings for seaside project.

import os
import logging

PROJECT_BASE = os.path.dirname(__file__)

ADMINS = (
    ('varikin', 'varikin@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False

MEDIA_ROOT = os.path.join(PROJECT_BASE, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'seaside.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_BASE, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'seaside.pages',
)

LOG_FILENAME = os.path.join(PROJECT_BASE, 'seaside.log')
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(module)s.%(funcName)s:%(message)s"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format=LOG_FORMAT)

try:
    from local_settings import *
except ImportError:
    pass

