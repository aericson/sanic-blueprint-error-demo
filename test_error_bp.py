import pytest
from sanic_testing import TestManager


@pytest.fixture
def test_client():
    from app import init_app

    app = init_app()

    TestManager(app)
    return app.test_client


def test_it(test_client):
    request, response = test_client.get("/")

    assert response.text == "OOops"
