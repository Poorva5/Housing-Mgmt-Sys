from os import getenv, path

from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

DEBUG = True

SITE_NAME = getenv('SITE_NAME')

SECRET_KEY = getenv("DJANGO_SECRET_KEY", 'DhFcyfg4CMJ7u1dSygWmrjousCriJ9fxuVDk67-Mh_DV8DFoU04')

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv('DJANGO_ADMIN_URL')
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBacken'
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')
DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL')
DOMAIN = getenv('DOMAIN')