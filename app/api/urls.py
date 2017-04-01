"""
This module contains blueprint and all endpoints in api.
"""

from flask import Blueprint
from flask_restful_swagger_2 import Api
from app.api.resources.sites import SitesResource, SiteResource, SiteByUrlResource


def get_blueprint():
    """Create blueprint"""

    blueprint = Blueprint('api', __name__)
    api = Api(blueprint, add_api_spec_resource=False)

    api.add_resource(SitesResource, '/sites', endpoint='sites')
    api.add_resource(SiteResource, '/site/<int:site_id>', endpoint='site')
    api.add_resource(SiteByUrlResource, '/site_by_url', endpoint='site_by_url')

    return api
