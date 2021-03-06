"""
Django settings for tutorial project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l(o-%vtgvw+*$aonrs06cfld+x7p7npjet&c(=p9rmopx=^xdf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.2', '127.0.0.1']

REST_SESSION_LOGIN = False
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tutorial',
]

DEFAULT_CHARSET='utf-8'

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'tutorial.auto_auth.Middleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'tutorial.disable_csrf.DisableCSRFMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tutorial.urls'

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

WSGI_APPLICATION = 'tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
    # '/var/www/static/',
]
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# 1. install python
# 2. install django
# 3. install react native expo

# 4. install pagkage python as following
# ex: pip install backports.shutil-get-terminal-size==1.0.0
#backports.shutil-get-terminal-size==1.0.0
#decorator==4.2.1
#Django==1.11
#djangorestframework==3.7.7
#enum34==1.1.6
#imutils==0.4.5
#ipdb==0.10.3
#ipython==5.5.0
#ipython-genutils==0.2.0
#numpy==1.14.0
#opencv-python==3.4.0.12
#pathlib2==2.3.0
#pdfkit==0.6.1
#pexpect==4.3.1
#pickleshare==0.7.4
#prompt-toolkit==1.0.15
#ptyprocess==0.5.2
#Pygments==2.2.0
#pytz==2017.3
#scandir==1.6
#scipy==1.0.0
#simplegeneric==0.8.1
#simplejson==3.13.2
#six==1.11.0
#traitlets==4.3.2
#wcwidth==0.1.7

# 5. install PDF lib https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
