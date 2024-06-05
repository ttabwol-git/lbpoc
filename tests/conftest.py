"""Main pytest configuration file"""

import os
import sys
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient

os.environ['TESTS_PATH'] = os.path.dirname(os.path.abspath(__file__))
os.environ['ROOT_PATH'] = os.path.join(os.environ['TESTS_PATH'], os.pardir)
sys.path.insert(0, os.environ['ROOT_PATH'])

# importing the main FastAPI app
from main import app

# Load the environment variables required for testing
load_dotenv(os.path.join(os.environ['CONFIG_PATH'], 'pytest.env'))


@pytest.fixture(scope="module")
def test_app():
    """Fixture for the FastAPI test app"""
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def auth_headers():
    """Fixture for the authorization headers"""
    yield {'Authorization': f'Bearer {os.environ['BEARER_TOKEN']}'}
