"""
Django settings for placelist project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


from os import environ

### Use these for web version
GEOS_LIBRARY_PATH = "{}/libgeos_c.so".format(environ.get('GEOS_LIBRARY_PATH'))
GDAL_LIBRARY_PATH = "{}/libgdal.so".format(environ.get('GDAL_LIBRARY_PATH'))
PROJ4_LIBRARY_PATH = "{}/libproj.so".format(environ.get('PROJ4_LIBRARY_PATH'))



### Use these for local version
# GEOS_LIBRARY_PATH = environ.get('GEOS_LIBRARY_PATH')
# GDAL_LIBRARY_PATH = environ.get('GDAL_LIBRARY_PATH')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'luyhm&$4n2&f3!cf%t955e!(j5sjfgnr7b0%33mn$fb*@finzp'

### I added a comment


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'tastypie',
    'bootstrapform',
    'rest_framework',
    'listr',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'placelist.urls'

WSGI_APPLICATION = 'placelist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'placelist',
        'USER': 'kevin',
        'PASSWORD': 'geodjango',
    }
}

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

        ],
    },
},]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

############
#   KEYS   #
############

INSTAGRAM_CLIENT_ID = ''
INSTAGRAM_CLIENT_SECRET = ''

GOOGLEMAP_API_KEY = ''
YAHOO_CONSUMER_KEY = ''
YAHOO_CONSUMER_SECRET = ''
YAHOO_APP_ID = ''

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''


FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''

GOOGLE_PLUS_APP_ID = ''
GOOGLE_PLUS_APP_SECRET = ''

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)



