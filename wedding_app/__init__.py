from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from wedding_app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'rsvp'
login_manager.login_message = ''

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from wedding_app.main.routes import main
    from wedding_app.guests.routes import guests
    app.register_blueprint(main)
    app.register_blueprint(guests)

    return app
