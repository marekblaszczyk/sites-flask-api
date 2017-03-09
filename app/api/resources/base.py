"""
This module contains definitions of base resource from which every other resource should inherit.
"""
from flask_restful import Resource
from app.lib.utils import serialize_data


class BaseResource(Resource):
    """This class define base resource of every resource object in api."""

    @staticmethod
    def serialize(data, schema=None, code=200, headers=None):
        """Serialize answer, add header, set return status code."""

        ret_headers = {}

        if headers:
            for header, value in headers.iteritems():
                ret_headers[header] = value

        if schema is not None:
            return serialize_data(schema, data), code, ret_headers
        else:
            return data, code, ret_headers
