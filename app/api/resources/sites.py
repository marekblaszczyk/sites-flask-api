# -*- coding: utf-8 -*-
"""
This module contains definitions of resources assosciated with article.
"""
from app.api.resources.base import BaseResource
from app.extensions import RPC
from app.api.serializers import SITES_SCHEMA


class SitesResource(BaseResource):
    """Resource for sites."""

    def get(self):
        """This method ask rpc service about all sites in mongo db."""

        sites = RPC.site_service.get_sites()
        return self.serialize(data=sites, schema=SITES_SCHEMA)
