import os

from eve import Eve
from flask import jsonify, request, session
from werkzeug.exceptions import ImATeapot

from app.authentication.jwt import encode_auth_token, decode_auth_token


HTTP_SUCCESS = 200
HTTP_BAD_REQUEST = 400
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_UNAUTHORIZED = 401

port = 5000
host = '127.0.0.1'

if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'

app = Eve()


@app.route('/hello')
def hello_world():
    people = [person["firstname"] + " " + person["lastname"] for person in app.data.driver.db['people'].find()]
    people_names = ", ".join(people)

    return 'hello world! People: ' + people_names


@app.route('/login', methods=['POST'])
def login():
    data = _get_json_data()

    # TODO retrieve user

    token = encode_auth_token(_get_secret(), 1)

    authorized_user = _build_authorization_response({"_id": 1}, token.decode('ascii'))
    return authorized_user


@app.route('/userFromToken', methods=['POST'])
def user_from_token():
    token = request.headers['Authorization']

    user_id = decode_auth_token(_get_secret(), token)
    if user_id is False:
        return jsonify({"success": False}), HTTP_UNAUTHORIZED

    return _build_authorization_response({"_id": user_id}, token)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('session_token', None)
    return jsonify({"success": True})


def _get_json_data():
    data = request.get_json()

    if not data:
        raise ImATeapot('Invalid JSON Request Data')

    return data


def _build_authorization_response(user, token):
    authorization = _build_authorization(user, token)

    return jsonify(authorization)


def _build_authorization(user, token):
    user_id = f'{user["_id"]}'

    return {
        'token': token,
        'user_id': user_id,
    }


def _get_secret():
    return os.environ.get('JWT_SECRET') or 'ThisShouldNotBeTheDefaultValue'


if __name__ == '__main__':
    app.run(host=host, port=port)
