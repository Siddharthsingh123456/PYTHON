from flask import Flask

from config import Config
from extensions import bcrypt, cors, db, jwt, migrate
from routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    register_blueprints(app)

    @app.get('/health')
    def health_check():
        return {"status": "ok"}, 200

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
