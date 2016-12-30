import pytest
import os

from distelli import Distelli


@pytest.fixture
def client():
    return Distelli(
        username=os.getenv('DISTELLI_USERNAME'),
        api_token=os.getenv('DISTELLI_API_TOKEN'),
    )
