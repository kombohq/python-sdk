"""Tests for synchronous context manager cleanup (e.g. Celery workers)."""

import asyncio

import pytest

from kombo import Kombo


class TestSyncContextManagerCleanup:
    """Ensure sync ``with Kombo(...)`` closes clients without asyncio errors."""

    def test_sync_context_exits_cleanly_without_event_loop(self):
        """No running loop: __exit__ must not raise."""

        def sync_worker():
            with Kombo(api_key="test-key"):
                pass

        sync_worker()

    def test_sync_context_exits_cleanly_after_exception_without_event_loop(self):
        """When the body raises, cleanup must not mask the original error."""

        def sync_worker():
            with pytest.raises(ValueError, match="original"):
                with Kombo(api_key="test-key"):
                    raise ValueError("original")

        sync_worker()

    def test_sync_context_exits_cleanly_when_nested_asyncio_loop_runs(self):
        """If a loop is running in the same thread, cleanup must still not raise."""

        async def run():
            def sync_section():
                with Kombo(api_key="test-key"):
                    pass

            sync_section()

        asyncio.run(run())
