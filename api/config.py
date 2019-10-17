from os import environ

postgres_local_base = 'postgresql://test_user:test@localhost/'
database_name = 'flask_auth_test'

class BaseConfig:
	DEBUG = False
    #SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DATABASE_URL="postgresql:///"

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
