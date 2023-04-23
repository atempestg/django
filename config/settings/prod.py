from .base import *

ALLOWED_HOSTS = ['43.200.190.244', 'atempest.hopto.org']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}