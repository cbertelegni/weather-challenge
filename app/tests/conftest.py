import pytest
import responses
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app, raise_server_exceptions = False) as client:
        yield client


@pytest.fixture(scope="function", autouse=True)
def mocked_responses():
    with responses.RequestsMock() as mock_requests:
        yield mock_requests