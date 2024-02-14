"""
Django settings for sitev project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from django.utils import timezone
from django.contrib.messages import constants as messages

now = timezone.now()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8hrhrhrh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#CSRF_TRUSTED_ORIGINS = ['']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'discordbot',
   
  
    
    'crispy_forms',
    'bootstrap4',
    'imagekit',
    'crispy_bootstrap4',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.discord',
    'django.contrib.humanize',
 
]




AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]



SOCIALACCOUNT_PROVIDERS = {
    'discord': {
        'SCOPE': [
            'identify',
            'email',
            'guilds',
            
            
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
    }


SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_FORMS = {
  
  'login': 'accounts.forms.MyLoginForm',
  
  
}
#store socialaccounts tokens in the database 
SOCIALACCOUNT_STORE_TOKENS = True
#mandatory means that the user cannot login after signing unless he verified his email address
ACCOUNT_EMAIL_VERIFICATION = "optional"

SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION


  #When signing up, let the user type in their email address twice to avoid typo's.
ACCOUNT_ADAPTER = 'sitev.account_adapter.NoNewUsersAccountAdapter'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert alert-secondary',
        messages.INFO: 'alert alert-info',
        messages.SUCCESS: 'alert alert-success',
        messages.WARNING: 'alert alert-warning',
        messages.ERROR: 'alert alert-danger',
 }

CRISPY_TEMPLATE_PACK = 'bootstrap4'




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sitev.urls'

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
    },
]

WSGI_APPLICATION = 'sitev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


LANGUAGE_CODE = 'en'



USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = [
  ('ar', ('Arabic')),
  ('en', ('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sitev/static')
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
#media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field





DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10mb = 10 * 1024 *1024
TEMP = os.path.join(BASE_DIR, 'media_cdn/temp')



TIME_ZONE = 'Egypt'





















API_ENDPOINT = 'https://discord.com/api/v10/oauth2/token'
CLIENT_ID = '920737996909723648'
CLIENT_SECRET = 'LgITRsI0DI-vkou6JC_GqOdLVklBBIte'
REFRESH_TOKEN = '2zEpGDsS33sb7eSRjQSdsEaOjYqBDx'
REDIRECT_URI = 'http://127.0.0.1:8000/account/discord/login/callback/'

