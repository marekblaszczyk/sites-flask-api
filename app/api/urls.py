"""
This module contains blueprint and all endpoints in api.
"""

from flask import Blueprint
from flask_restful_swagger_2 import Api
from app.api.resources.sites import SitesResource


BLUEPRINT = Blueprint('api', __name__)
api = Api(BLUEPRINT, api_version='0.1', api_spec_url='/api/swagger')

api.add_resource(SitesResource, '/sites', endpoint='sites')
