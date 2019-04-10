from flask import Flask, Blueprint, request

from engine import models
from engine.responses import ok, internal_error, not_implemented

engine = Blueprint('engine', __name__, url_prefix='')


@engine.route('/enhance', methods=['POST'])
def enhance():
    try:
        response = models.enhance(request.get_json())
        return response, ok()

    except NotImplementedError as nie:
        return not_implemented()

    except RuntimeError as re:
        return internal_error()
