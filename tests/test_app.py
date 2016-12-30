from fixtures import client


class TestApp(object):
    app_name = '_test_app'

    def setup_method(self, method):
        client_instance = client()
        self.__original_apps = [app['name'] for app in client_instance.apps()]
        if self.app_name not in self.__original_apps:
            client_instance.create_app(self.app_name)

    def teardown_method(self, method):
        client_instance = client()
        for app in client_instance.apps():
            if app['name'] not in self.__original_apps:
                print('delete_app', app['name'])
                client_instance.delete_app(app['name'])

    def test_apps(self, client):
        assert self.app_name in [app['name'] for app in client.apps()]

    def test_app(self, client):
        assert self.app_name == client.app(self.app_name)['name']

    def test_create_app(self, client):
        name = '_test_app_add'
        client.create_app(name)
        assert name in [app['name'] for app in client.apps()]

    def test_delete_app(self, client):
        client.delete_app(self.app_name)
        assert self.app_name not in [app['name'] for app in client.apps()]
