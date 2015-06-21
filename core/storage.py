from second import settings
# from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticRootS3BotoStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaRootS3BotoStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION