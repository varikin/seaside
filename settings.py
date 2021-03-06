# Django settings for seaside project.

import os
import logging

PROJECT_BASE = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('varikin', 'varikin@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',                      
        'USER': '',     
        'PASSWORD': '', 
        'HOST': '',     
        'PORT': '',
    }
}     

SECRET_KEY = '*23ie0kskkq!=!ud59ke^8cxyu($f79wlx!lm!v=@l$&xy)45_'


TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False

MEDIA_ROOT = os.path.join(PROJECT_BASE, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_BASE, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIR = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
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
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'ckeditor',
    'storages',

    # My apps
    'seaside.pages',
)

CKEDITOR_CONFIGS = {
    'default': {

        'toolbar': [
            [      'Cut', 'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline', 'Strike',
              '-', 'Subscript', 'Superscript',
              '-', 'Link', 'Unlink', 'Anchor', 'Image',
              '-', 'Format',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
            ],
            [      'HorizontalRule',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'Cut','Copy','Paste','PasteText','PasteFromWord',
              '-', 'SpecialChar',
              '-', 'Source',
              '-', 'About',
            ]
        ],
        'width': 840,
        'height': 300,
        'toolbarCanCollapse': False,
    }
}



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
   }
}

# Django Storage settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''


try:
    from local_settings import *
except ImportError:
    pass

