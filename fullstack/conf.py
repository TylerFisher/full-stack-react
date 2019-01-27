"""
Use this file to configure pluggable app settings and resolve defaults
with any overrides set in project settings.
"""

from django.conf import settings as project_settings

from .exceptions import FullstackConfigError


class Settings:
    pass


Settings.AUTH_DECORATOR = getattr(
    project_settings,
    "FULLSTACK_AUTH_DECORATOR",
    "django.contrib.auth.decorators.login_required",
)

Settings.SECRET_KEY = getattr(
    project_settings, "FULLSTACK_SECRET_KEY", "a-bad-secret-key"
)

Settings.AWS_ACCESS_KEY_ID = getattr(
    project_settings, "FULLSTACK_AWS_ACCESS_KEY_ID", None
)

Settings.AWS_SECRET_ACCESS_KEY = getattr(
    project_settings, "FULLSTACK_AWS_SECRET_ACCESS_KEY", None
)

Settings.AWS_REGION = getattr(project_settings, "FULLSTACK_AWS_REGION", None)

Settings.AWS_S3_BUCKET = getattr(
    project_settings, "FULLSTACK_AWS_S3_BUCKET", None
)

Settings.CLOUDFRONT_ALTERNATE_DOMAIN = getattr(
    project_settings, "FULLSTACK_CLOUDFRONT_ALTERNATE_DOMAIN", None
)

Settings.S3_UPLOAD_ROOT = getattr(
    project_settings, "FULLSTACK_S3_UPLOAD_ROOT", "uploads/fullstack"
)

Settings.API_AUTHENTICATION_CLASS = getattr(
    project_settings,
    "FULLSTACK_API_AUTHENTICATION_CLASS",
    "rest_framework.authentication.BasicAuthentication",
)

Settings.API_PERMISSION_CLASS = getattr(
    project_settings,
    "FULLSTACK_API_PERMISSION_CLASS",
    "rest_framework.permissions.IsAdminUser",
)

settings = Settings
