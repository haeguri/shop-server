import os

# BASE_DIR absolute path in local: /Users/haegyun/Proeject-django/second
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't1^bbq7w*8oqs90&_bmn$hd#%^i#u47lmc=d4f1knl+8o1c-^$'

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'snippets',
    'corsheaders',
    'post_office',
    'storages',
    'django_summernote',
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
    'TOKEN_SERIALIZER': 'snippets.serializers.TokenSerializer',
    'USER_DETAILS_SERIALIZER':'snippets.serializers.UserDetailsSerializer',
    'LOGIN_SERIALIZER':'snippets.serializers.LoginSerializer',
    'PASSWORD_RESET_SERIALIZER':'snippets.serializers.PasswordResetSerializer',
}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ladio',
        'USER': 'admin',
        'PASSWORD': '82307201',
    }
}

# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True

USE_L10N = True

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

EMAIL_BACKEND = 'post_office.EmailBackend'

# email 관련 세팅
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

AUTH_USER_MODEL = 'snippets.User'

# django all-auth package settings
ACCOUNT_ADAPTER = "second.adapters.MessageFreeAdapter"
SOCIALACCOUNT_ADAPTER = "second.adapters.SocialAccountAdapter"

ACCOUNT_AUTHENTICATION_METHOD = 'email'

# 빌트-인 장고 유저 모델에서의 "username" 필드 이름에 대응되는 커스텀 사용자 모델의 필드 이름.
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'nickname'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
# "True" 설정시 실제로 사용자 모델의 필드 이름이 "username"이라는 필드를 required 상태로 요구.
# 근데 "username"은 커스텀 사용자 모델에는 없는 필드.
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USERNAME_MIN_LENGTH = 4


#### test!!


STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_HOST = 's3-ap-northeast-1.amazonaws.com'
AWS_QUERYSTRING_AUTH = False

S3_URL = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '/imedia/'

STATICFILES_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (S3_URL, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (S3_URL, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'core.storage.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'core.storage.StaticRootS3BotoStorage'

ROOT_URLCONF = 'second.urls'

WSGI_APPLICATION = 'second.wsgi.application'

#
# STATIC_ROOT = 'staticfiles'
# # STATIC_URL = '/static/'
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR + '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_DEBUG = True
DEBUG = True

try:
    from second.local_settings import *
except ImportError:
    print("The local setting is not exists.")
    pass

