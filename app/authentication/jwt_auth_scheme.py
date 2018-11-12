import os

from eve.auth import TokenAuth

from app.authentication.jwt import decode_auth_token


class JwtAuthScheme(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        print(token, resource)
        user_id = decode_auth_token(_get_secret(), token)
        return user_id


def _get_secret():
    return os.environ.get('JWT_SECRET') or 'ThisShouldNotBeTheDefaultValue'
