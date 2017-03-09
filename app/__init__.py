"""
This is main module for app factory, it contains function
for configure app, initializes extensions.
"""
import os
from flask import Flask, jsonify
from app.exceptions import ApiException
from app.extensions import RPC


__all__ = ['app']


def create_app(config=None, config_file=None):
    """This factory function create app object with parameters send toi function."""

    app = Flask(__name__)

    configure_app(app, config, config_file)
    configure_extensions(app)

    blueprints = app.config['BLUEPRINTS']

    configure_blueprints(app, blueprints)
    configure_exceptions(app)

    return app


def configure_app(app, config=None, config_file=None):
    """
    This function configure app. Default config is from Config class.
    If you need, you can pass config file by parameter.
    """
    # http://flask.pocoo.org/docs/api/#configuration
    config_name = os.getenv('PUBLIC_API_CONFIG', 'DevelopmentConfig')
    app.config.from_object('config.' + config_name)

    # example file is config.cfg
    # http://flask.pocoo.org/docs/config/#instance-folders
    if config_file:
        additional_config = os.path.join(os.path.dirname(app.instance_path), config_file)
        app.config.from_pyfile(additional_config, silent=True)

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    """
    This function configures all extensions used in app.
    """
    RPC.init_app(app)


def configure_blueprints(app, blueprints):
    """
    This function configures blueprints which are passed to function.
    """

    for blueprint_config in blueprints:
        name, rest = None, {}

        if isinstance(blueprint_config, basestring):
            name = blueprint_config
        elif isinstance(blueprint_config, (list, tuple)):
            name = blueprint_config[0]
            rest.update(blueprint_config[1])
        else:
            raise Exception('Bad blueprint config.')

        add_blueprint(app, name, rest)


def add_blueprint(app, name, rest):
    """This function register blueprint in application app."""
    blueprint = import_variable(name, 'urls', 'BLUEPRINT')
    app.register_blueprint(blueprint, **rest)


def import_variable(blueprint_path, module, variable_name):
    """This function import package and returns blueprint to register."""
    path = '.'.join(['app'] + blueprint_path.split('.') + [module])
    mod = __import__(path, fromlist=[variable_name])
    return getattr(mod, variable_name)


def configure_exceptions(app):
    """
    This function configures exceptions which should be raised when error occurs.
    """

    @app.errorhandler(404)
    def handle_error(error):
        """This function handle 404 errors."""
        response = jsonify({
            "message": error.name,
            "status_code": 404
        })
        response.status_code = error.code
        return response

    @app.errorhandler(ApiException)
    def handle_api_exception(error):
        """This function handle errors from exceptions module."""
        response = jsonify(error.feedback)
        response.status_code = error.status_code
        return response

app = create_app()
