import boto3
from fullstack.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


def get_bucket():
    session = boto3.session.Session(
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')

    return s3.Bucket(settings.AWS_S3_BUCKET)


class Defaults(object):
    CACHE_HEADER = str('max-age=5')
    ROOT_PATH = 'elections'
    ACL = 'public-read'


defaults = Defaults


class StorageService(S3Boto3Storage):
    bucket_name = settings.AWS_S3_BUCKET
    access_key = settings.AWS_ACCESS_KEY_ID
    secret_key = settings.AWS_SECRET_ACCESS_KEY
    file_overwrite = True
    querystring_auth = False
    object_parameters = {
        'CacheControl': 'max-age=86400',
        'ACL': 'public-read',
    }
    custom_domain = settings.CLOUDFRONT_ALTERNATE_DOMAIN
    location = settings.S3_UPLOAD_ROOT
