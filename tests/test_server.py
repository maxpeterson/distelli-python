import pytest

from distelli import DistelliException
from fixtures import client


class TestServer(object):
    def test_servers(self, client):
        assert [] == client.servers()

    def test_server_does_not_exist(self, client):
        with pytest.raises(DistelliException) as exception:
            client.server('does-not-exist')

        assert 'Server does-not-exist not found' in str(exception.value)

    def test_delete_server_does_not_exist(self, client):
        with pytest.raises(DistelliException) as exception:
            client.delete_server('does-not-exist')
        assert 'Server does-not-exist not found' in str(exception.value)
