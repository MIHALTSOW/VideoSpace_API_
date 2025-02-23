from datetime import timedelta

import jwt
from django.utils import timezone
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework.authentication import BaseAuthentication

from Authorization_token.models import TokenForRegistration, AuthorizationUserOnToken


def delete_expired_tokens():
    expired_tokens = TokenForRegistration.objects.filter(created_at__lt=timezone.now() - timedelta(minutes=20))
    expired_tokens.delete()


def delete_user_without_password():
    users_without_password = AuthorizationUserOnToken.objects.filter(password=None)
    users_without_password.delete()


class AllowAnyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return True
