import pytest

from distelli import Distelli, DistelliException


class TestAuth(object):
    def test_authentication_with_no_credentials_raises(self):
        with pytest.raises(DistelliException) as exception:
            Distelli().apps()

        assert 'No authentication details provided.' in str(exception.value)

    def test_authentication_with_bad_credentials_raises(self):
        with pytest.raises(DistelliException) as exception:
            Distelli(username='any', api_token='another').apps()

        assert 'Request Authentication failed. Check your credentials.' in str(exception.value)

    def test_authentication_connection_raises(self):
        with pytest.raises(DistelliException) as exception:
            client = Distelli(username='any', api_token='another')
            client._endpoint = 'https://api.example.com/'
            client.apps()

        assert 'Failed to reach a server.' in str(exception.value)
