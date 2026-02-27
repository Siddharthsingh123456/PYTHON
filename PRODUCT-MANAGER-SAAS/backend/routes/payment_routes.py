from flask import Blueprint, request

from services.stripe_service import create_checkout_session
from utils.decorators import jwt_required_user


payment_bp = Blueprint('payment', __name__)


@payment_bp.post('/checkout')
@jwt_required_user
def checkout():
    payload = request.get_json() or {}
    return create_checkout_session(payload)
