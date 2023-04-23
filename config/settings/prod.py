from .base import *

ALLOWED_HOSTS = ['43.200.190.244', 'atempest.hopto.org']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'PASSWORD': ':giEcy%BPnNp1y<[D4WL(~qS83!LjVb`',
        'HOST': 'ls-2034d4cd826c7810dd78cdc78b7365e1197ad59f.cvkqqskmwouw.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}