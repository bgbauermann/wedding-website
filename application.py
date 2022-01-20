from wedding_app import create_app
from wedding_app import db

application = create_app()

if __name__ == '__main__':
    application.run()