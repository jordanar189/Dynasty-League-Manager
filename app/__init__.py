from flask import Flask

from .config import Config
from .main.routes import main_bp


def create_app(config_class: type[Config] = Config) -> Flask:
    """Application factory for scalable Flask app setup."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(main_bp)

    return app
