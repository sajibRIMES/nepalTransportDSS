"""
Django settings for APIs project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os,json,pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMLATE_DIR=Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v@%=p!xeh2dmu&-$%3syu(-pd25*1z^9*#kkl$25m0*uvnhuow'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    # 'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    # 'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'corsheaders',
    'rest_framework',

    'observed.apps.ObservedConfig',
    'climatology.apps.ClimatologyConfig',
    'forecast.apps.ForecastConfig',
    'transport.apps.TransportConfig',
    'observedClimatology.apps.ObservedclimatologyConfig'
]

GDAL_LIBRARY_PATH='/opt/homebrew/Cellar/gdal/3.6.2/lib/libgdal.dylib'
GEOS_LIBRARY_PATH='/opt/homebrew/Cellar/geos/3.11.1/lib/libgeos_c.dylib'
# DEFAULT_DB_ALIAS='localPostGIS'

CORS_ALLOW_ALL_ORIGINS=True
# CORS_ORIGIN_ALLOW_ALL=True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 51
# }

ROOT_URLCONF = 'APIs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True,
        'DIRS': [os.path.join(TEMLATE_DIR, 'templates/rest_framework')],

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'loaders':[
                 'django.template.loaders.app_directories.Loader',
                 'django.template.loaders.filesystem.Loader',
                 'admin_tools.template_loaders.Loader',
                ]
        },
    },
]


# ADMIN_TOOLS_MENU = 'observed.menu.apiMenu'

# WSGI_APPLICATION = 'APIs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = json.load(open(os.path.join(BASE_DIR,'dbconfig.json'),'r'))
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

DATABASE_ROUTERS = [
    'APIs.dbrouters.observedRouter',
    'APIs.dbrouters.observedClimatologyRouter',
    'APIs.dbrouters.forecastRouter',
    'APIs.dbrouters.transportRouter',
    'APIs.dbrouters.postgresRouter'
    
]

# DATABASES = 


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'