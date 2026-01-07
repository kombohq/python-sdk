"""Tests for Kombo ATS Jobs API."""

from inline_snapshot import snapshot
from tests.conftest import MockContext


class TestKomboATSJobsAPI:
    """Test Kombo ATS Jobs API."""

    def test_should_make_correct_http_request_for_get_jobs(self):
        """Test that get_jobs makes correct HTTP request."""
        ctx = MockContext()

        # Mock the API endpoint
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
        jobs = ctx.kombo.ats.get_jobs()
        if jobs is not None:
            _ = jobs.next()  # Consume first page

        # Verify and snapshot the request details
        request = ctx.get_last_request()
        assert request.path == snapshot('/v1/ats/jobs?page_size=100&include_deleted=false&ignore_unsupported_filters=false')

