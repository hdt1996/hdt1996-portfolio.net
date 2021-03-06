"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


server_config = open(os.path.join(BASE_DIR,'server_config.json'),'r')
conf_dict = json.load(server_config)

HOST = conf_dict["host"]
DOMAIN = conf_dict["domain"].replace('https://','')
www = conf_dict["www"].replace('https://','')
server_config.close()

PROJECT_PATH=BASE_DIR

SECRET_KEY=os.environ.get('SECRET_KEY','HDT121919964085')

DEBUG = bool(int(os.environ.get('DEBUG',0)))
ALLOWED_HOSTS = [HOST,DOMAIN,www]
ALLOWED_HOSTS_ENV= os.environ.get('ALLOWED_HOSTS')

if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))
DEFAULT_AUTO_FIELD= 'django.db.models.BigAutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.store',
    'frontend.dj_frontend',
    'API.spotify',
    'rest_framework',
    'corsheaders',
]

SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'https://hdt1996-portfolio.net',
    'https://www.hdt1996-portfolio.net',
    f'http://{HOST}:8001',
    f'http://{HOST}:3000',
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
SESSION_CCOKIE_DOMAIN = '127.0.0.1'
ROOT_URLCONF = 'backend.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': \
        [
            os.path.join(BASE_DIR,'backend/templates'),
            os.path.join(BASE_DIR,'frontend/build')
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'storedb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': HOST,
        'PORT': '6432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':4}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



STATIC_URL='/static/'
STATIC_ROOT='/vol/web/static'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'backend/static')]
USER_MEDIA_ROOT = os.path.join(BASE_DIR, 'frontend/media')
USER_MEDIA_URL='/media/'

if DEBUG==1:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    REACT_ROOT= os.path.join(BASE_DIR,"frontend/build/") 
    REACTSTATIC_ROOT=os.path.join(BASE_DIR,"frontend/build/static")


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.SessionAuthentication'
    ]
}
""" 
MEDIA_URL='/media/'
REACT_URL='/react/'
REACTSTATIC_URL='/react/static/' 
"""
"""
REACT_ROOT= "/webserver/frontend/build"
REACTSTATIC_ROOT="/webserver/frontend/build/static" 
"""
"""     
REACTSRC_ROOT= "/webserver/frontend/src"
REACTSRC_ROOT= os.path.join(BASE_DIR,"frontend/src")
REACTSRC_URL='/react/src/' 
"""
