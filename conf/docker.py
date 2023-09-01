"""The module indented to extend and override settings.py via the environment variables."""

import os

from dotenv import load_dotenv

from conf.settings import *

load_dotenv()

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')

DEBUG = os.getenv('DEBUG', '').lower() == 'true'

SECRET_KEY = os.environ['SECRET_KEY']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('PG_HOST', '127.0.0.1'),
        'PORT': os.getenv('PG_PORT', '5432'),
        'NAME': os.getenv('PG_NAME', 'weather'),
        'USER': os.getenv('PG_USER', 'postgres'),
        'PASSWORD': os.getenv('PG_PASSWORD', 'postgres'),
    }
}

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

WEATHER_API_CITY = os.getenv('WEATHER_API_CITY', 'rostov-na-donu')

WEATHER_API_DAYS = int(os.getenv('WEATHER_API_DAYS', '14'))
