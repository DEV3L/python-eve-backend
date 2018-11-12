from datetime import datetime, timedelta

import jwt


def encode_auth_token(secret_key, user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=30),
            'iat': datetime.utcnow(),
            'sub': user_id
        }

        return jwt.encode(payload, secret_key, algorithm='HS256')
    except Exception as e:
        return e


def decode_auth_token(secret_key, auth_token):
    try:
        payload = jwt.decode(auth_token, secret_key)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
