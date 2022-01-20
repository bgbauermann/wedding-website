from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from wedding_app.config import DevConfig, ProdConfig
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'rsvp'
login_manager.login_message = ''
if os.environ.get('WEDDING_APP_ENV') == 'PROD':
    config = ProdConfig
else:
    config = DevConfig

def create_app(config_class=config):
    application = Flask(__name__)
    application.config.from_object(config)

    db.init_app(application)
    migrate = Migrate(application, db)
    login_manager.init_app(application)

    from wedding_app.main.routes import main
    from wedding_app.guests.routes import guests
    application.register_blueprint(main)
    application.register_blueprint(guests)

    return application
