from flask import Blueprint, request

from services.ml_service import predict_price
from utils.decorators import jwt_required_user


ml_bp = Blueprint('ml', __name__)


@ml_bp.post('/predict')
@jwt_required_user
def predict():
    payload = request.get_json() or {}
    return predict_price(payload)
