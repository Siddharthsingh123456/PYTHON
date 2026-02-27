from functools import wraps

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request


def jwt_required_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity() or {}
        if identity.get('role') != 'admin':
            return {'error': 'admin access required'}, 403
        return func(*args, **kwargs)

    return wrapper
