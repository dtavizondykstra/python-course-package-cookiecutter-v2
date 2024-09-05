"""
Module provides example fixtures for pytest.

It includes fixtures that are used across multiple test cases.
"""

from uuid import uuid4

import pytest

from tests.consts import PROJECT_DIR


@pytest.fixture(scope="session")
def test_session_id() -> str:
    """
    Generate a unique session ID for the test session.

    This fixture creates a unique session ID by combining the project directory name
    with a truncated UUID. The session ID is used to identify the test session.

    Returns
    -------
    str
        A unique session ID.

    """
    test_session_id = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
