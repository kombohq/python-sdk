"""Test fixtures and helpers for Kombo SDK tests."""

from typing import Optional, Dict, Any, List
import json
import re
import pytest
import respx
import httpx
from kombo import Kombo


# Sentinel value to distinguish between "not provided" and "explicitly None"
_UNSET = object()


class CapturedRequest:
    """Represents a captured HTTP request."""

    def __init__(self, method: str, path: str, headers: Dict[str, str], body: Optional[Any] = None):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body


class MockContext:
    """Test context for mocking HTTP requests and capturing request details."""

    def __init__(self, api_key: Optional[str] = None, integration_id: Any = _UNSET):
        """
        Initialize test context.

        :param api_key: API key to use (defaults to "test-api-key")
        :param integration_id: Integration ID to use. Defaults to "test-integration-id" if not provided.
                               Pass None explicitly to omit the integration_id from SDK initialization.
        """
        self._api_key = api_key or "test-api-key"
        
        # Determine integration_id value
        if integration_id is _UNSET:
            # Not provided, use default
            id_to_use = "test-integration-id"
        else:
            # Use provided value (could be None, a string, etc.)
            id_to_use = integration_id
        
        self._captured_requests: List[CapturedRequest] = []
        
        # Initialize SDK
        if id_to_use is None:
            self.kombo = Kombo(api_key=self._api_key)
        else:
            self.kombo = Kombo(api_key=self._api_key, integration_id=id_to_use)

    def mock_endpoint(
        self,
        method: str,
        path: str,
        response: Dict[str, Any],
    ) -> None:
        """
        Mock an HTTP endpoint.

        :param method: HTTP method (GET, POST, PUT, DELETE, PATCH)
        :param path: URL path (e.g., "/v1/ats/jobs")
        :param response: Response dict with 'body', optional 'statusCode', and optional 'headers'
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
            if request.method != "GET" and request.content:
                try:
                    # Try to parse as JSON first
                    request_body = json.loads(request.content.decode())
                except (json.JSONDecodeError, UnicodeDecodeError):
                    # Fall back to raw string if not valid JSON
                    request_body = request.content.decode()

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
            route = respx.request(
                method=method,
                url__regex=re.compile(f"^{re.escape(base_url)}(\\?.*)?$"),
            )
        else:
            route = respx.request(
                method=method,
                url=base_url,
            )

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
        """Clear captured requests and reset mocks.
        
        Note: respx is managed by the reset_respx fixture, but we need to
        clear registered routes between calls within the same test.
        """
        self._captured_requests.clear()
        respx.clear()


@pytest.fixture(autouse=True)
def reset_respx():
    """Reset respx mocks before and after each test."""
    respx.start()
    yield
    respx.stop()
    respx.clear()

