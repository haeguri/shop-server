"""
Django settings for second project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

# BASE_DIR absolute path in local: /Users/haegyun/Proeject-django/second
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't1^bbq7w*8oqs90&_bmn$hd#%^i#u47lmc=d4f1knl+8o1c-^$'

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition


SITE_ID = 1

INSTALLED_APPS = (
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'snippets',
    # 현재 cart app은 사용하지 않음.
    #'cart',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'second.middleware.CustomSessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'second.custom_auth.TokenSerializer',
    'USER_DETAILS_SERIALIZER':'second.custom_auth.UserDetailsSerializer',
    'LOGIN_SERIALIZER':'second.custom_auth.LoginSerializer',
}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ladio',
        'USER': 'admin',
         # 실제 제품에서는 비밀번호 숨겨야 함.
        'PASSWORD': '82307201',
    }
}


ROOT_URLCONF = 'second.urls'

WSGI_APPLICATION = 'second.wsgi.application'

# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True

USE_L10N = True

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/media/'

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
)

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['*']

# email 관련 세팅
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'haegyun821@gmail.com'
EMAIL_HOST_PASSWORD = 'dlfvmf26'
EMAIL_PORT = 587
EMAIL_USE_TLS = True




AUTH_USER_MODEL = 'snippets.User'

# django all-auth package settings

ACCOUNT_ADAPTER = "second.adapters.MessageFreeAdapter"

ACCOUNT_AUTHENTICATION_METHOD = 'email'

# 빌트-인 장고 유저 모델에서의 "username" 필드 이름에 대응되는 커스텀 사용자 모델의 필드 이름.
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'nickname'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
# "True" 설정시 실제로 사용자 모델의 필드 이름이 "username"이라는 필드를 required 상태로 요구.
# 근데 "username"은 커스텀 사용자 모델에는 없는 필드.
ACCOUNT_USERNAME_REQUIRED = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DEBUG = True

STATIC_ROOT = 'staticfiles'

DEBUG = True

try:
    from second.local_settings import *
except ImportError:
    print("local setting file is not exists.")
    pass

