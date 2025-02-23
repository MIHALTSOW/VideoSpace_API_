import jwt
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import AuthenticationFailed

from .utils import get_user


class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b"authorization" in headers:
            token_name, token = headers[b"authorization"].decode().split()
            if token_name == "Bearer":
                try:
                    decoded_data = jwt.decode(token, options={"verify_signature": False})
                    scope["user"] = await get_user(decoded_data["user_id"])
                except (jwt.InvalidTokenError, AuthenticationFailed):
                    scope["user"] = AnonymousUser()
            else:
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()
        return await super().__call__(scope, receive, send)
