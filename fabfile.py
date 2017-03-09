# -*- coding: utf-8 -*-
"""
This module defines all commands used to work and manage with service.
"""
from fabric.api import local, prefix


def rs():
    """This function executes developer server."""
    with prefix('export API_ENV="DevelopmentConfig"'):
        local('python manage.py runserver -r')
