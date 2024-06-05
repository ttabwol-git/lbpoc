"""Test Module for Topics Service"""

import os
import pytest
from fastapi.testclient import TestClient
from starlette import status


class TestTopics:
    """Test class for Topics Service"""

    @pytest.mark.parametrize(
        "data, expected_status",
        [
            (
                    {"topic": "sales", "description": "This is a test description with more than 10 characters."},
                    status.HTTP_200_OK
            ),
            (
                    {"topic": "pricing", "description": "Another test description with more than 10 characters."},
                    status.HTTP_200_OK
            ),
            (
                    {"test": "test"},
                    status.HTTP_422_UNPROCESSABLE_ENTITY
            ),
            (
                    {"topic": "test", "description": "This is a test description with more than 10 characters."},
                    status.HTTP_422_UNPROCESSABLE_ENTITY
            ),
            (
                    {"topic": "sales", "description": "test"},
                    status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        ],
    )
    def test_submit(self, test_app: TestClient, auth_headers: dict, data: dict, expected_status: int):

        # Reset the Slack channel to the test channel
        os.environ['SLACK_CHANNEL'] = '#test'

        response = test_app.post('api/topics/submit', json=data, headers=auth_headers)
        assert response.status_code == expected_status
