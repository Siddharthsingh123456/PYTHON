from flask import Blueprint, request

from services.product_service import create_product, list_products, update_product_price
from utils.decorators import jwt_required_user


product_bp = Blueprint('products', __name__)


@product_bp.get('/')
@jwt_required_user
def get_products():
    return list_products()


@product_bp.post('/')
@jwt_required_user
def add_product():
    payload = request.get_json() or {}
    return create_product(payload)


@product_bp.patch('/<int:product_id>/price')
@jwt_required_user
def patch_product_price(product_id):
    payload = request.get_json() or {}
    return update_product_price(product_id, payload)
