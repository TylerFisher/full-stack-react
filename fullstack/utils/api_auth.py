from fullstack.conf import settings
from django.conf import settings as project_settings
from django.contrib.auth.models import AnonymousUser
from django.utils.decorators import method_decorator
from rest_framework import authentication, exceptions


class TokenAPIAuthentication(authentication.BaseAuthentication):
    """
    DRF custom authentication class for viewsets.

    Uses app's secret key to authenticate AJAX requests.
    """
    def authenticate(self, request):
        # Don't enforce if DEBUG
        if project_settings.DEBUG:
            return (AnonymousUser, None)
        try:
            # Token should be prefixed with string literal "Token" plus
            # whitespace, e.g., "Token <TOKEN>".
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        except:
            raise exceptions.AuthenticationFailed(
                'No token or incorrect token format')

        if token == settings.SECRET_KEY:
            return (AnonymousUser, None)
        raise exceptions.AuthenticationFailed('Unauthorized')
