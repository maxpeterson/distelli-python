"""
Client for Distelli REST API
https://www.distelli.com/docs/api/
"""

import json
import os
from requests import Request, Session, ConnectionError, HTTPError


class DistelliException(Exception):
    pass


class Distelli(object):
    _endpoint = 'https://api.distelli.com/'

    def __init__(self, username=None, api_token=None):
        """
        Create authenticated API client.
        Provide `username` and `api_token`.
        """
        if username is None:
            username = os.getenv('DISTELLI_USERNAME')
        if api_token is None:
            api_token = os.getenv('DISTELLI_API_TOKEN')

        if username is None or api_token is None:
            raise DistelliException('No authentication details provided.')

        self.__username, self.__api_token = username, api_token

    def __rest_helper(self, url, data=None, params=None, method='GET'):
        """
        Handles requests to the Distelli API, defaults to GET requests if none
        provided.
        """

        url = "{endpoint}/{username}{url}?apiToken={api_token}".format(
            endpoint=self._endpoint,
            username=self.__username,
            url=url,
            api_token=self.__api_token,
        )
        headers = {
            'Content-Type': 'application/json'
        }

        request = Request(
            method=method,
            url=url,
            headers=headers,
            data=json.dumps(data),
            params=params,
        )

        prepared_request = request.prepare()

        result = self.__request_helper(prepared_request)

        return result

    @staticmethod
    def __request_helper(request):
        """Handles firing off requests and exception raising."""
        try:
            session = Session()
            handle = session.send(request)

        except ConnectionError:
            raise DistelliException('Failed to reach a server.')

        except HTTPError:  # pragma: no cover
            raise DistelliException('Invalid response.')

        response = handle.json() if handle.content else {}

        if 400 <= handle.status_code:
            raise DistelliException(response)

        return response

    # Apps

    def apps(self):
        """Get a list of all apps in your account."""
        return self.__rest_helper('/apps', method='GET')['apps']

    def app(self, app_name):
        """Get the details for a specific app in your account."""
        url = '/apps/{name}'.format(name=app_name)
        return self.__rest_helper(url, method='GET')['app']

    def create_app(self, app_name, description=''):
        """Create an application in your account."""
        data = {'description': description}
        url = '/apps/{name}'.format(name=app_name)
        return self.__rest_helper(url, data, method='PUT')['app']

    def delete_app(self, app_name):
        """Delete an application in your Distelli account."""
        url = '/apps/{name}'.format(name=app_name)
        return self.__rest_helper(url, method='DELETE')
