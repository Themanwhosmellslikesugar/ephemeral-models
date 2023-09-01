"""WSGI config for weather project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.docker')

application = get_wsgi_application()
