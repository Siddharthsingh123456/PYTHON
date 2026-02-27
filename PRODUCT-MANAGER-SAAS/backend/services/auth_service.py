from flask_jwt_extended import create_access_token

from extensions import bcrypt, db
from models.user import User


def register_user(payload):
    email = payload.get('email')
    password = payload.get('password')
    if not email or not password:
        return {'error': 'email and password are required'}, 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {'error': 'email already exists'}, 409

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return {'message': 'user created', 'user': user.to_dict()}, 201


def login_user(payload):
    email = payload.get('email')
    password = payload.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return {'error': 'invalid credentials'}, 401

    token = create_access_token(identity={'id': user.id, 'role': user.role})
    return {'access_token': token, 'user': user.to_dict()}, 200
