# -*- coding: utf-8 -*-
"""
Module with Api serializers.
"""
from marshmallow import Schema, fields


class SitesSchema(Schema):
    """Serialize class for sites."""

    site_id = fields.Int()
    title = fields.Str()
    content = fields.Str()
    url = fields.Str()


class SiteSchema(Schema):
    """Serialize class for site."""

    site_id = fields.Int()
    title = fields.Str()
    content = fields.Str()
    url = fields.Str()


SITES_SCHEMA = SitesSchema(many=True)
SITE_SCHEMA = SiteSchema()
