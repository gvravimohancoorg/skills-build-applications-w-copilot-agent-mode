from flask import Flask

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    # Register blueprints
    from . import main
    app.register_blueprint(main.bp)

    return app
