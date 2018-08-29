import os


class Config(object):
    """Parent class configuration """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DATABASE_NAME = 'stackoverflow'
    

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
    DEBUG = False
    TESTING = False


CONFIGS = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig 
}

#key = Config.SECRET_KEY