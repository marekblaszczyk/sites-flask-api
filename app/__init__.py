"""
This is main module for app factory, it contains function
for configure app, initializes extensions.
"""
import os
from flask import Flask, jsonify
from app.exceptions import ApiException


__all__ = ['app']


def create_app(config=None, config_file=None):
    """This factory function create app object with parameters send toi function."""

    app = Flask(__name__)

    blueprints = app.config['BLUEPRINTS']

    return app