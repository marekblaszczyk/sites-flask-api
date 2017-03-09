import os


class BaseConfig(object):
    """This is base class of api configuration."""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ADMINS = ('marek.blaszczyk@gmail.com')

    # set your own
    SECRET_KEY = 'ziequahsh4Eediji4shee7aequ9Geehu'
    CSRF_SESSION_KEY = 'eeg3ioDaechohk5rievoothae5ooshib'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    ERROR_404_HELP = False

    BLUEPRINTS = (
        'api',
    )
    RESTFUL_JSON = {'ensure_ascii': False, 'indent': 4, 'encoding': 'utf-8'}
    CONFIG = 'base'
    NAMEKO_AMQP_URI = 'amqp://guest:guest@localhost'


class TestingConfig(BaseConfig):
    """This is config class for testing purposes."""

    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    CONFIG = 'testing'


class DevelopmentConfig(BaseConfig):
    """This is config class for developers."""

    DEBUG = True
    CONFIG = 'development'
    SERVER_ADDRESS = 'localhost'
    PORT = 5002


class ProductionConfig(BaseConfig):
    """This is config class with production settings."""

    DEBUG = False
    PROPAGATE_EXCEPTIONS = True
    CONFIG = 'production'
