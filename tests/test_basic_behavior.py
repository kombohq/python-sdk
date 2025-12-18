"""Tests for basic SDK behavior."""

from inline_snapshot import snapshot
from tests.conftest import MockContext


class TestBasicSDKBehavior:
    """Test basic SDK behavior."""

    def test_should_include_api_key_in_authorization_header(self):
        """Test that API key is included in Authorization header."""
        ctx = MockContext(api_key="my-custom-api-key")

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
        ctx = MockContext(
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
        ctx = MockContext(
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
        ctx = MockContext()

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
        jobs = ctx.kombo.ats.get_jobs(
            statuses=["OPEN", "CLOSED"],
            ids=["CPDifhHr7izJhKHmGPkXqknC", "J7znt8TJRiwPVA7paC2iCh8u"],
        )
        if jobs is not None:
            _ = jobs.next()  # Consume first page

        # Verify and snapshot the request details
        request = ctx.get_last_request()
        assert request.path == snapshot(
            '/v1/ats/jobs?page_size=100&include_deleted=false&ids=CPDifhHr7izJhKHmGPkXqknC%2CJ7znt8TJRiwPVA7paC2iCh8u&statuses=OPEN%2CCLOSED'
        )

    def test_should_correctly_encode_boolean_query_parameters(self):
        """Test that boolean query parameters are correctly encoded."""
        ctx = MockContext()

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

    def test_should_correctly_serialize_post_request_body(self):
        """Test that POST request bodies are correctly serialized."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="POST",
            path="/v1/ats/jobs/test-job-id/applications",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "id": "app-123",
                        "remote_id": "remote-app-123",
                        "outcome": "PENDING",
                        "rejection_reason_name": None,
                        "rejected_at": None,
                        "current_stage_id": "stage-1",
                        "job_id": "test-job-id",
                        "candidate_id": "candidate-456",
                        "custom_fields": {},
                        "remote_url": "https://example.com/application/123",
                        "changed_at": "2024-01-01T00:00:00Z",
                        "remote_deleted_at": None,
                        "remote_created_at": "2024-01-01T00:00:00Z",
                        "remote_updated_at": "2024-01-01T00:00:00Z",
                        "current_stage": None,
                        "job": None,
                        "candidate": None,
                    },
                    "warnings": [],
                },
            },
        )

        # Make the API call
        ctx.kombo.ats.create_application(
            job_id="test-job-id",
            candidate={
                "first_name": "Jane",
                "last_name": "Smith",
                "email_address": "jane.smith@example.com",
            },
        )

        # Verify request body is correctly serialized
        request = ctx.get_last_request()
        assert request.method == "POST"
        assert request.body == snapshot(
            {
                "candidate": {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "email_address": "jane.smith@example.com",
                }
            }
        )

