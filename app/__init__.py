import configparser
import secrets

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    config = configparser.ConfigParser()
    config.read('config.ini')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('database', 'uri')
    app.secret_key = secrets.token_urlsafe(16)
    db.init_app(app)

    print(f"####\nSuccesfully connected to database {app.config['SQLALCHEMY_DATABASE_URI']}\n####")

    from .controllers.agent_controller import agent_bp
    from .controllers.fleet_controller import fleet_bp
    from .controllers.home_controller import home_bp
    from .controllers.universe_controller import universe_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(agent_bp)
    app.register_blueprint(universe_bp)
    app.register_blueprint(fleet_bp)

    return app