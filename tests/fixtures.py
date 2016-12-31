import pytest
import os

from distelli import Distelli


@pytest.fixture
def client():
    return Distelli(
        username=os.getenv('DISTELLI_TEST_USERNAME'),
        api_token=os.getenv('DISTELLI_TEST_API_TOKEN'),
    )
