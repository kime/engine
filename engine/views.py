from traceback import print_stack

from flask import Blueprint, request
from flask_httpauth import HTTPBasicAuth
from passlib.handlers.sha2_crypt import sha512_crypt

from engine import models, config
from engine.responses import ok, internal_error, not_implemented

auth = HTTPBasicAuth()
engine = Blueprint('engine', __name__, url_prefix='')


@auth.verify_password
def verify_password(user, secret):
    """

    :param auth_token:
    :param password:
    :return:
    """
    # Check if auth_token is valid
    actual_user, secret_hash = config.backend_credentials()
    if not user == actual_user or not sha512_crypt.verify(secret, secret_hash):
        return False
    return True


@auth.login_required
@engine.route('/enhance', methods=['POST'])
def enhance():
    try:
        response = models.enhance(request.get_json())
        return response, ok()

    except NotImplementedError as nie:
        print_stack(nie)
        return not_implemented()

    except RuntimeError as re:
        print_stack(re)
        return internal_error()
