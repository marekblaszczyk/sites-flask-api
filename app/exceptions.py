# -*- coding: utf-8 -*-
"""This module gathers all exceptions"""
import json
from nameko.exceptions import registry

EXCEPTIONS_DICT = {}


def remote_error(exc_path):
    """
    Decorator that registers remote exception with matching ``exc_path``
    to be deserialized to decorated exception instance, rather than
    wrapped in ``RemoteError``.

    """
    def wrapper(exc_type):
        registry[exc_path] = exc_type
        return exc_type
    return wrapper


class ApiException(Exception):
    """Base class for every custom exception."""
    status_code = 400
    message = 'ApiError'
    origin = 'api-gateway'
    feedback = {}

    def __init__(self, exc=None, *args, **kwargs):
        self.feedback['message'] = self.message
        if exc is not None:
            self.feedback = json.loads(exc)
        self.feedback['origin'] = self.feedback.get('origin', self.origin)
        if 'message' in kwargs and kwargs['message'] is not None:
            self.feedback['message'] = kwargs['message']
        self.feedback['message'] = self.feedback.get('message', self.message)
        self.feedback['status_code'] = self.status_code

        Exception.__init__(self)


@remote_error('app.exceptions.NotFound')
class NotFoundException(ApiException):
    """This error is raised by microservice when element is not found in resource."""
    message = 'Item not found'
    status_code = 404


@remote_error('app.exceptions.NoArgument')
class NoArgumentException(ApiException):
    """This error is raised by article microservice when no specified parameters are send."""
    message = 'Invalid argument'
    status_code = 400


@remote_error('app.exceptions.Error')
class ErrorException(ApiException):
    """This error should be raise by article when any other error does not fit."""
    message = 'Error'
    status_code = 500


@remote_error('app.exceptions.ElementExists')
class ElementExistsException(ApiException):
    """This error should be raise by microservice when an element already exist in db."""
    message = 'Element exists'
    status_code = 409
