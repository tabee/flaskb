class Config(object):
    CONFIG_VARIANTE = 'Config'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    CONFIG_VARIANTE = 'Production'
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    CONFIG_VARIANTE = 'Developement'
    HOST = '127.0.0.1'
    DEBUG = True

class TestingConfig(Config):
    CONFIG_VARIANTE = 'Testing'
    TESTING = True