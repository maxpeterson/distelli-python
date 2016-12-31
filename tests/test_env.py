import pytest

from distelli import DistelliException
from fixtures import client


class TestApp(object):
    app_name = '_test_app'
    env_name = '_test_env'

    def setup_method(self, method):
        client_instance = client()

        self.__original_apps = [app['name'] for app in client_instance.apps()]
        if self.app_name not in self.__original_apps:
            client_instance.create_app(self.app_name)

        self.__original_envs = [env['name'] for env in client_instance.envs()]
        if self.env_name not in self.__original_envs:
            client_instance.create_env(self.app_name, self.env_name)

    def teardown_method(self, method):
        client_instance = client()
        for env in client_instance.envs():
            if env['name'] not in self.__original_envs:
                client_instance.delete_env(env['name'])
        for app in client_instance.apps():
            if app['name'] not in self.__original_apps:
                client_instance.delete_app(app['name'])

    def test_envs(self, client):
        assert self.env_name in [env['name'] for env in client.envs()]

    def test_env(self, client):
        assert self.env_name == client.env(self.env_name)['name']

    def test_create_env(self, client):
        name = '_test_env_add'
        client.create_env(self.app_name, name)
        assert name in [env['name'] for env in client.envs()]

    def test_delete_env(self, client):
        client.delete_env(self.env_name)
        assert self.env_name not in [env['name'] for env in client.envs()]

    def test_add_env_server(self, client):
        servers = client.add_env_servers(self.env_name, [])
        assert servers == []

    def test_remove_env_server(self, client):
        servers = client.remove_env_servers(self.env_name, [])
        assert servers == []

    def test_env_does_not_exist(self, client):
        with pytest.raises(DistelliException) as exception:
            client.env('does-not-exist')

        assert 'Env does-not-exist not found' in str(exception.value)

    def test_delete_env_does_not_exist(self, client):
        with pytest.raises(DistelliException) as exception:
            client.delete_env('does-not-exist')

        assert 'Env does-not-exist not found' in str(exception.value)
