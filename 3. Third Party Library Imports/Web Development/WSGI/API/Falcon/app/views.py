"""
This package contains the views used in the falcon RESTful API
"""

from falcon import request, response  # these imports are not called directly, but I use the side effects for type setting

easy_response = "This is a string that will be sent back on a successful GET request to this endpoint"


class EndpointOne:
    @staticmethod
    def on_get(req: request, resp: response):  # falcon requires the req and resp variables to exist
        resp.media = easy_response


class EndpointTwo:
    @staticmethod
    def on_get(req: request, resp: response):
        resp.media = easy_response
