from flask import jsonify


def ok():
    """
    Standard response for successful HTTP requests
    :return: 200 OK
    """
    return 200


def bad_request(message="Bad Request"):
    """
    Response when the server cannot the request due to an apparent client error
    :param message: explanation of the error situation
    :return: 400 Bad Request
    """
    return jsonify({"message": message}), 400


def forbidden(message="Forbidden"):
    """
    Response when the user might not have the necessary permissions for a resource
    :param message: explanation of the error situation
    :return: 403 Forbidden
    """
    return jsonify({"message": message}), 403


def internal_error(message="Internal Server Error"):
    """
    Response given when an unexpected condition was encountered
    :param message: explanation of the error situation
    :return: 500 Internal Server Error
    """
    return jsonify({"message": message}), 500
