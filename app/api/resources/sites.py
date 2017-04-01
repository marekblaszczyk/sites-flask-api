# -*- coding: utf-8 -*-
"""
This module contains definitions of resources assosciated with article.
"""
from flask import request
from app.api.resources.base import BaseResource
from app.extensions import RPC
from app.api.serializers import SITES_SCHEMA, SITE_SCHEMA


class SitesResource(BaseResource):
    """Resource for sites."""

    def get(self):
        """This method ask rpc service about all sites in mongo db."""

        sites = RPC.site_service.get_sites()
        return self.serialize(data=sites, schema=SITES_SCHEMA)


class SiteResource(BaseResource):
    """Resource for one site."""

    def get(self, site_id):
        """Get method ask microservice about page by id."""

        site = RPC.site_service.get_site(site_id=site_id, url=None)
        return self.serialize(data=site, schema=SITE_SCHEMA)


class SiteByUrlResource(BaseResource):
    """Resource for one site."""

    def get(self):
        """Get method ask microservice about page with url."""

        url = request.args.get('url', None)

        site = RPC.site_service.get_site(site_id=None, url=url)
        return self.serialize(data=site, schema=SITE_SCHEMA)
