"""Test fixtures and helpers for Kombo SDK tests."""

from typing import Optional, Dict, Any, List
import json
import respx
import httpx
from kombo import Kombo


class CapturedRequest:
    """Represents a captured HTTP request."""

    def __init__(self, method: str, path: str, headers: Dict[str, str], body: Optional[Any] = None):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body


class TestContext:  # noqa: D101
    """Test context for mocking HTTP requests and capturing request details."""

    def __init__(self, api_key: Optional[str] = None, integration_id: Optional[str] = None):
        """
        Initialize test context.

        :param api_key: API key to use (defaults to "test-api-key")
        :param integration_id: Integration ID to use (defaults to "test-integration-id" if not explicitly None)
        """
        self._api_key = api_key or "test-api-key"
        # If integration_id is explicitly None, don't pass it; otherwise use default
        self._integration_id = integration_id if integration_id is not None else "test-integration-id"
        self._captured_requests: List[CapturedRequest] = []
        
        # Initialize SDK
        if integration_id is None:
            self.kombo = Kombo(api_key=self._api_key)
        else:
            self.kombo = Kombo(api_key=self._api_key, integration_id=self._integration_id)

    def mock_endpoint(
        self,
        method: str,
        path: str,
        response: Dict[str, Any],
        delay_response_ms: Optional[int] = None,
    ) -> None:
        """
        Mock an HTTP endpoint.

        :param method: HTTP method (GET, POST, PUT, DELETE, PATCH)
        :param path: URL path (e.g., "/v1/ats/jobs")
        :param response: Response dict with 'body', optional 'statusCode', and optional 'headers'
        :param delay_response_ms: Optional delay in milliseconds before responding
        """
        status_code = response.get("statusCode", 200)
        body = response.get("body")
        response_headers = response.get("headers", {})

        # Set up Content-Type header for JSON responses if not provided
        if isinstance(body, dict) and "Content-Type" not in response_headers:
            response_headers = {**response_headers, "Content-Type": "application/json"}

        # Prepare response content
        if isinstance(body, (dict, list)):
            content = json.dumps(body).encode()
        elif isinstance(body, str):
            content = body.encode()
        else:
            content = b""

        # Create response function that captures request
        def create_response(request: httpx.Request) -> httpx.Response:
            # Capture request details
            query_string = request.url.query.decode() if request.url.query else ""
            full_path = request.url.path + (f"?{query_string}" if query_string else "")
            
            # Read body for non-GET requests
            request_body = None
            if request.method != "GET":
                try:
                    # Try to get content from request
                    if hasattr(request, "_content"):
                        body_bytes = request._content
                    elif hasattr(request, "content"):
                        body_bytes = request.content
                    else:
                        # Try reading from stream
                        body_bytes = request.read()
                    
                    if body_bytes:
                        try:
                            if isinstance(body_bytes, bytes):
                                request_body = json.loads(body_bytes.decode())
                            else:
                                request_body = json.loads(body_bytes)
                        except (json.JSONDecodeError, UnicodeDecodeError, TypeError):
                            if isinstance(body_bytes, bytes):
                                request_body = body_bytes.decode()
                            else:
                                request_body = body_bytes
                except Exception:
                    # If we can't read the body, that's okay
                    pass

            captured = CapturedRequest(
                method=request.method,
                path=full_path,
                headers=dict(request.headers),
                body=request_body,
            )
            self._captured_requests.append(captured)

            return httpx.Response(
                status_code=status_code,
                headers=response_headers,
                content=content,
            )

        # Create the mock route
        # For GET requests, match any query parameters using regex
        # For other methods, match exact path
        base_url = f"https://api.kombo.dev{path}"
        if method == "GET":
            # Match the base path, allowing any query parameters
            import re
            route = respx.request(
                method=method,
                url__regex=re.compile(f"^{re.escape(base_url)}(\\?.*)?$"),
            )
        else:
            route = respx.request(
                method=method,
                url=base_url,
            )

        # Handle delay if specified
        if delay_response_ms is not None:
            def delayed_response(request: httpx.Request) -> httpx.Response:
                import time
                # Sleep to simulate delay - this will cause timeout if timeout_ms < delay_response_ms
                time.sleep(delay_response_ms / 1000.0)
                return create_response(request)
            route.mock(side_effect=delayed_response)
        else:
            route.mock(side_effect=create_response)

    def get_requests(self) -> List[CapturedRequest]:
        """Get all captured requests."""
        return list(self._captured_requests)

    def get_last_request(self) -> CapturedRequest:
        """Get the last captured request."""
        if not self._captured_requests:
            raise RuntimeError("No requests captured!")
        return self._captured_requests[-1]

    def clear(self) -> None:
        """Clear captured requests and reset mocks."""
        self._captured_requests.clear()
        respx.stop()
        respx.clear()
        respx.start()  # Restart respx so new mocks can be registered


# Pytest fixtures
import pytest


@pytest.fixture(autouse=True)
def reset_respx():
    """Reset respx mocks before and after each test."""
    respx.start()
    yield
    respx.stop()
    respx.clear()

