import os




class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_NAME = 'stackoverflow_lite'
    

class DevelopmentConfig(Config):
    """Configuration fro Development."""
    DEBUG = True
    DATABASE_NAME = 'stackoverflow_lite'
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = "test_stackoverflow"
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class ProductionConfig(Config):
    """Configration for Production"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

app_config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    staging=StagingConfig,
    production=ProductionConfig,
    default=ProductionConfig
)
