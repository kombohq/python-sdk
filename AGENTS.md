# Testing Setup

Tests use pytest with `respx` for HTTP mocking and `inline-snapshot` for assertions.

**TestContext helper** (`tests/conftest.py`):
- `ctx = TestContext(api_key="...", integration_id="...")` - creates SDK instance
- `ctx.mock_endpoint(method, path, response)` - mocks HTTP endpoints
- `ctx.get_last_request()` - captures request details (path, headers, body)
- `ctx.clear()` - resets mocks between calls

**Running tests**:
- `mise run test` or `uv run pytest tests/ -v`
- `mise run test:update` - update snapshots
- Use `snapshot(...)` from `inline-snapshot` for assertions

