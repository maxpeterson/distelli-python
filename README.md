# Python Distelli

This is a client for the Distelli REST API. It currently allows you to fetch existing app info, as well as create and delete applications.

### Getting started

`distelli-python` depends on the `requests` library.

Install the library:

    pip install distelli

Import the module:

	from distelli import Distelli

Provide username and api\_token credentials:

    client = Distelli(username=YOUR_USERNAME, api_token=YOUR_API_TOKEN)

## Application Operations

### View your existing applications:

Just run:

	apps = client.apps()

Results appear as a Python dict:

    [{'api_url': 'https://api.distelli.com/youraccount/apps/test_app',
      'builds_url': 'https://api.distelli.com/youraccount/apps/test_app/builds',
      'created': '2016-12-30T18:07:50.284Z',
      'deployments_url': 'https://api.distelli.com/youraccount/apps/test_app/deployments',
      'description': None,
      'html_url': 'https://www.distelli.com/youraccount/apps/test_app',
      'latest_build': None,
      'latest_release': None,
      'name': 'test_app',
      'owner': 'youraccount',
      'releases_url': 'https://api.distelli.com/youraccount/apps/test_app/releases'},
     {'api_url': 'https://api.distelli.com/youraccount/apps/test_app2',
      'builds_url': 'https://api.distelli.com/youraccount/apps/test_app2/builds',
      'created': '2016-12-30T18:24:07.511Z',
      'deployments_url': 'https://api.distelli.com/youraccount/apps/test_app2/deployments',
      'description': 'Another test app',
      'html_url': 'https://www.distelli.com/youraccount/apps/test_app2',
      'latest_build': None,
      'latest_release': None,
      'name': 'test_app2',
      'owner': 'youraccount',
      'releases_url': 'https://api.distelli.com/youraccount/apps/test_app2/releases'}]

### Get details for a specific application

	client.app('test_app2')


Results are the same as `apps()` above, but only show the app specified.

### Create an application

Careful with this one!

    client.create_app('test_app3', 'Description of the application')

Results are the same as `app()` above, but only show the app specified.

### Delete an application

Careful with this one!

    client.delete_app('test_app3')


## Testing

To run the tests you will need a Distelli account and you will need to know your Distelli username and API token. As described in https://www.distelli.com/docs/api/getting-started-with-distelli-api

The tests will create and remove artifacts in your account.

Create a virtualenv (e.g. `mkvirtualenv --python=$(which python3) distelli-python`)

Install the requirements. `pip install -r requirements.txt`



Run the tests with your username and API token set using the environment variables DISTELLI_USERNAME and DISTELLI_API_TOKEN:

    DISTELLI_USERNAME=<username> DISTELLI_API_TOKEN=<api_token> make test
