from flask import Flask

from app.extensions import bcrypt, celery, cors, db, jwt, ma
from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_api(app)

    init_celery(app)

    return app


def init_celery(app=None):
    celery.conf.update(app.config.get("CELERY", {}))

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    from .auth import auth_bp

    app.register_blueprint(auth_bp)


def register_api(app):
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")
