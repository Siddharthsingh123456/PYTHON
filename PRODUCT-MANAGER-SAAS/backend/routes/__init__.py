from routes.admin_routes import admin_bp
from routes.auth_routes import auth_bp
from routes.ml_routes import ml_bp
from routes.payment_routes import payment_bp
from routes.product_routes import product_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(payment_bp, url_prefix='/api/payment')
    app.register_blueprint(ml_bp, url_prefix='/api/ml')
