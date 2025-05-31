from flask import Flask
from .cache import cache
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cache.init_app(app)

    from .routes.main import main_bp
    from .routes.projects import projects_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)

    return app
