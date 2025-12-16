"""Tests for basic SDK behavior."""

import pytest
from inline_snapshot import snapshot
from tests.conftest import TestContext


class TestBasicSDKBehavior:
    """Test basic SDK behavior."""

    def test_should_include_api_key_in_authorization_header(self):
        """Test that API key is included in Authorization header."""
        ctx = TestContext(api_key="my-custom-api-key")

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/jobs",
            response={
                "body": {
                    "status": "success",
                    "data": {"results": [], "next": None},
                },
            },
        )

        jobs = ctx.kombo.ats.get_jobs()
        if jobs is not None:
            _ = jobs.next()  # Consume first page

        request = ctx.get_last_request()
        assert request.headers.get("authorization") == snapshot("Bearer my-custom-api-key")

    def test_should_include_integration_id_in_x_integration_id_header_when_specified(self):
        """Test that X-Integration-Id header is included when specified."""
        ctx = TestContext(
            api_key="test-key",
            integration_id="my-integration-123",
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/jobs",
            response={
                "body": {
                    "status": "success",
                    "data": {"results": [], "next": None},
                },
            },
        )

        jobs = ctx.kombo.ats.get_jobs()
        if jobs is not None:
            _ = jobs.next()  # Consume first page

        request = ctx.get_last_request()
        assert request.headers.get("x-integration-id") == snapshot("my-integration-123")

    def test_should_not_include_x_integration_id_header_when_not_provided(self):
        """Test that X-Integration-Id header is not included when not provided."""
        ctx = TestContext(
            api_key="test-key",
            integration_id=None,
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/jobs",
            response={
                "body": {
                    "status": "success",
                    "data": {"results": [], "next": None},
                },
            },
        )

        jobs = ctx.kombo.ats.get_jobs()
        if jobs is not None:
            _ = jobs.next()  # Consume first page

        request = ctx.get_last_request()
        # When integration ID is None, the header should not be set
        assert request.headers.get("x-integration-id") is None

    def test_should_correctly_encode_comma_separated_query_parameters(self):
        """Test that comma-separated query parameters are correctly encoded."""
        ctx = TestContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/jobs",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [],
                        "next": None,
                    },
                },
            },
        )

        # Make the API call
        _jobs = ctx.kombo.ats.get_jobs(
            statuses=["OPEN", "CLOSED"],
            ids=["CPDifhHr7izJhKHmGPkXqknC", "J7znt8TJRiwPVA7paC2iCh8u"],
        )

        # Verify and snapshot the request details
        request = ctx.get_last_request()
        assert request.path == snapshot(
            '/v1/ats/jobs?page_size=100&include_deleted=false&ids=CPDifhHr7izJhKHmGPkXqknC%2CJ7znt8TJRiwPVA7paC2iCh8u&statuses=OPEN%2CCLOSED'
        )

    def test_should_correctly_encode_boolean_query_parameters(self):
        """Test that boolean query parameters are correctly encoded."""
        ctx = TestContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/jobs",
            response={
                "body": {
                    "status": "success",
                    "data": {"results": [], "next": None},
                },
            },
        )

        # Test with boolean true
        jobs_with_deleted = ctx.kombo.ats.get_jobs(include_deleted=True)
        if jobs_with_deleted is not None:
            _ = jobs_with_deleted.next()  # Consume first page

        request_with_deleted = ctx.get_last_request()
        assert "include_deleted=true" in request_with_deleted.path

        ctx.clear()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/jobs",
            response={
                "body": {
                    "status": "success",
                    "data": {"results": [], "next": None},
                },
            },
        )

        # Test with boolean false
        jobs_without_deleted = ctx.kombo.ats.get_jobs(include_deleted=False)
        if jobs_without_deleted is not None:
            _ = jobs_without_deleted.next()  # Consume first page

        request_without_deleted = ctx.get_last_request()
        assert "include_deleted=false" in request_without_deleted.path

