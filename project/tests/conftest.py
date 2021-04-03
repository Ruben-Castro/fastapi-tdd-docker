import os
import pytest

from starlette.testclient import TestClient

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


# fixtures are reusable objects for tests.
# They have a scope which indicates how often the feature
# is invoked

# functions - once per test function
# class - once pre test class
# module once per test module
# session once per test session

@pytest.fixture(scope="module")
def test_app():
    # basically all code before the yield statement
    # is test setup and all code
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client
