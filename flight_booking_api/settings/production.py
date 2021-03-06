import os
import dj_database_url

from dotenv import load_dotenv
from .base import *


load_dotenv()

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES['default'] = dj_database_url.config(default=os.getenv('POSTGRES_URL'))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
