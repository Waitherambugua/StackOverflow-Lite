import os
import datetime


class Config(object):
    """Parent class configuration """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DATABASE_NAME = 'stackoverflow'
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=10)

class DevelopmentConfig(Config):
    """Configuration for Development."""
    DEBUG = True
    DATABASE_NAME = 'stackoverflow'


class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = "test_stackoverflow"



class ProductionConfig(Config):
    """Configration for Production"""

    TESTING = False


app_config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig
}

#key = Config.SECRET_KEY
