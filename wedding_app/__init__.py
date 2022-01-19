from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from wedding_app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'rsvp'
login_manager.login_message = ''

def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from wedding_app.main.routes import main
    from wedding_app.guests.routes import guests
    application.register_blueprint(main)
    application.register_blueprint(guests)

    return application
