from flask import Blueprint, request

from services.auth_service import login_user, register_user


auth_bp = Blueprint('auth', __name__)


@auth_bp.post('/register')
def register():
    payload = request.get_json() or {}
    return register_user(payload)


@auth_bp.post('/login')
def login():
    payload = request.get_json() or {}
    return login_user(payload)
