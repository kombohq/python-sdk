"""Tests for Kombo ATS Jobs API."""

from inline_snapshot import snapshot
from tests.conftest import TestContext


class TestKomboATSJobsAPI:
    """Test Kombo ATS Jobs API."""

    def test_should_make_correct_http_request_for_get_jobs(self):
        """Test that getJobs makes correct HTTP request."""
        ctx = TestContext()

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
        _jobs = ctx.kombo.ats.get_jobs()

        # Verify and snapshot the request details
        request = ctx.get_last_request()
        assert request.path == snapshot("/v1/ats/jobs?include_deleted=false&page_size=100")

