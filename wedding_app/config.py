import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
  
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('RDS_USERNAME')}:{os.environ.get('RDS_PASSWORD')}@{os.environ.get('RDS_HOSTNAME')}/{os.environ.get('RDS_DB_NAME')}"
    DEBUG = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    DEBUG = True