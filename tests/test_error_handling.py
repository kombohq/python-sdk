"""Tests for error handling."""

import pytest
from inline_snapshot import snapshot
from tests.conftest import MockContext
from kombo.errors import (
    KomboAtsError,
    KomboHrisError,
    KomboGeneralError,
    SDKDefaultError,
    ResponseValidationError,
)


class TestErrorHandling:
    """Test error handling behavior."""

    class TestATSEndpoints:
        """Test ATS endpoint error handling."""

        def test_returns_kombo_ats_error_for_platform_rate_limit_errors(self):
            """Test that KomboAtsError is returned for platform rate limit errors."""
            ctx = MockContext()

            ctx.mock_endpoint(
                method="GET",
                path="/v1/ats/jobs",
                response={
                    "status_code": 429,
                    "body": {
                        "status": "error",
                        "error": {
                            "code": "PLATFORM.RATE_LIMIT_EXCEEDED",
                            "title": "Rate limit exceeded",
                            "message": "You have exceeded the rate limit. Please try again later.",
                            "log_url": "https://app.kombo.dev/logs/abc123",
                        },
                    },
                },
            )

            with pytest.raises(KomboAtsError) as exc_info:
                jobs = ctx.kombo.ats.get_jobs()
                if jobs is not None:
                    _ = jobs.next()  # Consume first page

            error = exc_info.value
            assert str(error) == snapshot("You have exceeded the rate limit. Please try again later.")
            assert error.data.error.code == snapshot("PLATFORM.RATE_LIMIT_EXCEEDED")
            assert error.data.error.title == snapshot("Rate limit exceeded")
            assert error.data.error.message == snapshot("You have exceeded the rate limit. Please try again later.")
            assert error.data.error.log_url == snapshot("https://app.kombo.dev/logs/abc123")
            assert error.data.status == snapshot("error")

        def test_returns_kombo_ats_error_for_ats_specific_job_closed_errors(self):
            """Test that KomboAtsError is returned for ATS-specific job closed errors."""
            ctx = MockContext()

            ctx.mock_endpoint(
                method="POST",
                path="/v1/ats/jobs/test-job-id/applications",
                response={
                    "status_code": 400,
                    "body": {
                        "status": "error",
                        "error": {
                            "code": "ATS.JOB_CLOSED",
                            "title": "Job is closed",
                            "message": "Cannot create application for a closed job. The job must be in an open state.",
                            "log_url": "https://app.kombo.dev/logs/ghi789",
                        },
                    },
                },
            )

            with pytest.raises(KomboAtsError) as exc_info:
                ctx.kombo.ats.create_application(
                    job_id="test-job-id",
                    candidate={
                        "first_name": "John",
                        "last_name": "Doe",
                        "email_address": "john.doe@example.com",
                    },
                )

            error = exc_info.value
            assert str(error) == snapshot(
                "Cannot create application for a closed job. The job must be in an open state."
            )
            assert error.data.error.code == snapshot("ATS.JOB_CLOSED")
            assert error.data.error.title == snapshot("Job is closed")
            assert error.data.error.message == snapshot(
                "Cannot create application for a closed job. The job must be in an open state."
            )
            assert error.data.error.log_url == snapshot("https://app.kombo.dev/logs/ghi789")
            assert error.data.status == snapshot("error")

    class TestHRISEndpoints:
        """Test HRIS endpoint error handling."""

        def test_returns_kombo_hris_error_for_integration_permission_errors(self):
            """Test that KomboHrisError is returned for integration permission errors."""
            ctx = MockContext()

            ctx.mock_endpoint(
                method="GET",
                path="/v1/hris/employees",
                response={
                    "status_code": 403,
                    "body": {
                        "status": "error",
                        "error": {
                            "code": "INTEGRATION.PERMISSION_MISSING",
                            "title": "Permission missing",
                            "message": "The integration is missing required permissions to access this resource.",
                            "log_url": "https://app.kombo.dev/logs/hris-def456",
                        },
                    },
                },
            )

            with pytest.raises(KomboHrisError) as exc_info:
                employees = ctx.kombo.hris.get_employees()
                if employees is not None:
                    _ = employees.next()  # Consume first page

            error = exc_info.value
            assert str(error) == snapshot(
                "The integration is missing required permissions to access this resource."
            )
            assert error.data.error.code == snapshot("INTEGRATION.PERMISSION_MISSING")
            assert error.data.error.title == snapshot("Permission missing")
            assert error.data.error.message == snapshot(
                "The integration is missing required permissions to access this resource."
            )
            assert error.data.error.log_url == snapshot("https://app.kombo.dev/logs/hris-def456")
            assert error.data.status == snapshot("error")

    class TestAssessmentEndpoints:
        """Test Assessment endpoint error handling."""

        def test_returns_kombo_ats_error_for_platform_input_validation_errors(self):
            """Test that KomboAtsError is returned for platform input validation errors."""
            ctx = MockContext()

            ctx.mock_endpoint(
                method="GET",
                path="/v1/assessment/orders/open",
                response={
                    "status_code": 400,
                    "body": {
                        "status": "error",
                        "error": {
                            "code": "PLATFORM.INPUT_INVALID",
                            "title": "Input invalid",
                            "message": "The provided input is invalid or malformed.",
                            "log_url": "https://app.kombo.dev/logs/assessment-xyz",
                        },
                    },
                },
            )

            with pytest.raises(KomboAtsError) as exc_info:
                orders = ctx.kombo.assessment.get_open_orders()
                if orders is not None:
                    _ = orders.next()  # Consume first page

            error = exc_info.value
            # Assessment uses KomboAtsError for errors
            assert str(error) == snapshot("The provided input is invalid or malformed.")
            assert error.data.error.code == snapshot("PLATFORM.INPUT_INVALID")
            assert error.data.error.title == snapshot("Input invalid")
            assert error.data.error.message == snapshot("The provided input is invalid or malformed.")
            assert error.data.error.log_url == snapshot("https://app.kombo.dev/logs/assessment-xyz")
            assert error.data.status == snapshot("error")

    class TestGeneralEndpoints:
        """Test General endpoint error handling."""

        def test_returns_kombo_general_error_for_authentication_errors(self):
            """Test that KomboGeneralError is returned for authentication errors."""
            ctx = MockContext()

            ctx.mock_endpoint(
                method="GET",
                path="/v1/check-api-key",
                response={
                    "status_code": 401,
                    "body": {
                        "status": "error",
                        "error": {
                            "code": "PLATFORM.AUTHENTICATION_INVALID",
                            "title": "Authentication invalid",
                            "message": "The provided API key is invalid or expired.",
                            "log_url": "https://app.kombo.dev/logs/general-auth-123",
                        },
                    },
                },
            )

            with pytest.raises(KomboGeneralError) as exc_info:
                ctx.kombo.general.check_api_key()

            error = exc_info.value
            # General endpoints use KomboGeneralError for errors
            assert str(error) == snapshot("The provided API key is invalid or expired.")
            assert error.data.error.code == snapshot("PLATFORM.AUTHENTICATION_INVALID")
            assert error.data.error.title == snapshot("Authentication invalid")
            assert error.data.error.message == snapshot("The provided API key is invalid or expired.")
            assert error.data.error.log_url == snapshot("https://app.kombo.dev/logs/general-auth-123")
            assert error.data.status == snapshot("error")

    class TestUnexpectedResponseFormats:
        """Test handling of unexpected response formats."""

        class TestSDKDefaultErrorForNonJSONResponses:
            """Test SDKDefaultError thrown for non-JSON responses."""

            def test_handles_plain_text_500_error_from_load_balancer(self):
                """Test handling of plain text 500 error from load balancer."""
                ctx = MockContext()

                ctx.mock_endpoint(
                    method="GET",
                    path="/v1/ats/jobs",
                    response={
                        "status_code": 500,
                        "body": "500 Internal Server Error",
                    },
                )

                with pytest.raises(SDKDefaultError) as exc_info:
                    jobs = ctx.kombo.ats.get_jobs()
                    if jobs is not None:
                        _ = jobs.next()  # Consume first page

                error = exc_info.value
                assert str(error) == snapshot(
                    'Unexpected response received: Status 500 Content-Type "". Body: 500 Internal Server Error'
                )

            def test_handles_plain_text_502_bad_gateway_error(self):
                """Test handling of plain text 502 bad gateway error."""
                ctx = MockContext()

                ctx.mock_endpoint(
                    method="GET",
                    path="/v1/hris/employees",
                    response={
                        "status_code": 502,
                        "body": "502 Bad Gateway",
                        "headers": {
                            "Content-Type": "text/plain",
                        },
                    },
                )

                with pytest.raises(SDKDefaultError) as exc_info:
                    employees = ctx.kombo.hris.get_employees()
                    if employees is not None:
                        _ = employees.next()  # Consume first page

                error = exc_info.value
                assert str(error) == snapshot(
                    'Unexpected response received: Status 502 Content-Type text/plain. Body: 502 Bad Gateway'
                )

            def test_handles_html_error_page_from_nginx(self):
                """Test handling of HTML error page from nginx."""
                ctx = MockContext()

                html_error_page = """<!DOCTYPE html>
<html>
<head><title>503 Service Temporarily Unavailable</title></head>
<body>
<center><h1>503 Service Temporarily Unavailable</h1></center>
<hr><center>nginx/1.18.0</center>
</body>
</html>"""

                ctx.mock_endpoint(
                    method="POST",
                    path="/v1/ats/jobs/test-job-id/applications",
                    response={
                        "status_code": 503,
                        "body": html_error_page,
                    },
                )

                with pytest.raises(SDKDefaultError) as exc_info:
                    ctx.kombo.ats.create_application(
                        job_id="test-job-id",
                        candidate={
                            "first_name": "John",
                            "last_name": "Doe",
                            "email_address": "john.doe@example.com",
                        },
                    )

                error = exc_info.value
                assert str(error) == snapshot(
                    """\
Unexpected response received: Status 503 Content-Type "". Body: <!DOCTYPE html>
<html>
<head><title>503 Service Temporarily Unavailable</title></head>
<body>
<center><h1>503 Service Temporarily Unavailable</h1></center>
<hr><center>nginx/1.18.0</center>
</body>
</html>\
"""
                )

            def test_handles_empty_response_body_with_error_status_code(self):
                """Test handling of empty response body with error status code."""
                ctx = MockContext()

                ctx.mock_endpoint(
                    method="GET",
                    path="/v1/check-api-key",
                    response={
                        "status_code": 500,
                        "body": "",
                    },
                )

                with pytest.raises(SDKDefaultError) as exc_info:
                    ctx.kombo.general.check_api_key()

                error = exc_info.value
                assert str(error) == snapshot('Unexpected response received: Status 500 Content-Type "". Body: ""')

            def test_handles_unexpected_content_type_header(self):
                """Test handling of unexpected Content-Type header."""
                ctx = MockContext()

                # Response with unexpected Content-Type
                ctx.mock_endpoint(
                    method="GET",
                    path="/v1/ats/applications",
                    response={
                        "status_code": 500,
                        "body": "Server error occurred",
                        "headers": {
                            "Content-Type": "text/xml",
                        },
                    },
                )

                with pytest.raises(SDKDefaultError) as exc_info:
                    applications = ctx.kombo.ats.get_applications()
                    if applications is not None:
                        _ = applications.next()  # Consume first page

                error = exc_info.value
                assert str(error) == snapshot(
                    'Unexpected response received: Status 500 Content-Type text/xml. Body: Server error occurred'
                )

        def test_handles_unexpected_json_structure_in_error_response(self):
            """Test handling of unexpected JSON structure in error response (ResponseValidationError)."""
            ctx = MockContext()

            # Valid JSON but unexpected structure (not matching Kombo error format)
            unexpected_json = {
                "errorCode": "500",
                "errorMessage": "Internal server error",
                "timestamp": "2024-01-01T00:00:00Z",
            }

            ctx.mock_endpoint(
                method="GET",
                path="/v1/ats/jobs",
                response={
                    "status_code": 500,
                    "body": unexpected_json,
                },
            )

            with pytest.raises(ResponseValidationError) as exc_info:
                jobs = ctx.kombo.ats.get_jobs()
                if jobs is not None:
                    _ = jobs.next()  # Consume first page

            error = exc_info.value
            # Valid JSON but unexpected structure triggers ResponseValidationError
            assert "Response validation failed" in str(error)


