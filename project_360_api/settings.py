from pathlib import Path
import os
from sshtunnel import SSHTunnelForwarder
import atexit

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$j02h*zgm^g@ye*$1@fkebf$&2t071wyn889b@j3x7%m&*7th3'
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'project_360_api',
    'project_summary',
    'project_kpi',
    'project_milestone',
    'django_filters',
    "corsheaders",
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

ROOT_URLCONF = 'project_360_api.urls'

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

WSGI_APPLICATION = 'project_360_api.wsgi.application'

# SSH configuration
SSH_HOST = '13.127.164.68'
SSH_PORT = 22
SSH_USER = 'ubuntu'
# SSH_PRIVATE_KEY_PATH = r"keys\data.pem"
SSH_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'keys','data.pem')

# MySQL configuration
MYSQL_HOST = '10.10.0.52'
MYSQL_PORT = 3306
MYSQL_USER = 'kepnath'
MYSQL_PASSWORD = '@#Kepnath@2024'
MYSQL_DB = 'haqdarshak-aggregates'

# SSH Tunnel setup
tunnel = SSHTunnelForwarder(
    (MYSQL_HOST, MYSQL_PORT),
    ssh_username=SSH_USER,
    ssh_pkey=SSH_PRIVATE_KEY_PATH,
    remote_bind_address=(MYSQL_HOST, MYSQL_PORT),
    local_bind_address=('localhost', SSH_PORT)
   
)

# Start the tunnel
tunnel.start()

# Update the DATABASES setting with the tunnel's local port
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv(MYSQL_DB,'haqdarshak-aggregates'),
        'USER': os.getenv(MYSQL_USER,'kepnath'),
        'PASSWORD': os.getenv(MYSQL_PASSWORD,'@#Kepnath@2024'),
        'HOST': os.getenv(MYSQL_HOST,'localhost'),
         'PORT': tunnel.local_bind_port or 3306
    }
}

atexit.register(tunnel.stop)



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
CORS_ALLOW_ALL_ORIGINS = True