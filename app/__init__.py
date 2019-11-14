from flask import Flask
from config import Config


def create_app(configuration=Config):
    """Flask App Instance"""

    app = Flask(__name__)
    app.config.from_object(configuration)

    from app.models import db, csrf, migrate

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    from app.views.base import base

    app.register_blueprint(base)
    return app
