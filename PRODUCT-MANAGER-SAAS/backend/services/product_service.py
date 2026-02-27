from extensions import db
from models.price_history import PriceHistory
from models.product import Product


def list_products():
    products = Product.query.order_by(Product.created_at.desc()).all()
    return {'products': [p.to_dict() for p in products]}, 200


def create_product(payload):
    name = payload.get('name')
    sku = payload.get('sku')
    current_price = payload.get('current_price')

    if not all([name, sku]) or current_price is None:
        return {'error': 'name, sku and current_price are required'}, 400

    product = Product(name=name, sku=sku, current_price=float(current_price))
    db.session.add(product)
    db.session.commit()
    return {'message': 'product created', 'product': product.to_dict()}, 201


def update_product_price(product_id, payload):
    product = Product.query.get_or_404(product_id)
    new_price = payload.get('new_price')
    if new_price is None:
        return {'error': 'new_price is required'}, 400

    old_price = product.current_price
    product.current_price = float(new_price)

    history = PriceHistory(product_id=product.id, old_price=old_price, new_price=product.current_price)
    db.session.add(history)
    db.session.commit()

    return {'message': 'price updated', 'product': product.to_dict()}, 200
