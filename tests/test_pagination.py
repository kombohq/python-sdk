"""Tests for pagination behavior."""

from datetime import datetime
from tests.conftest import MockContext


class TestPaginationBehavior:
    """Test pagination behavior."""

    def test_should_iterate_through_multiple_pages(self):
        """Test that SDK can iterate through multiple pages of results."""
        ctx = MockContext()

        # Mock 3 pages of results
        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag1",
                                "remote_id": None,
                                "name": "Tag 1",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                            {
                                "id": "tag2",
                                "remote_id": None,
                                "name": "Tag 2",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": "cursor_page2",
                    },
                },
            },
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag3",
                                "remote_id": None,
                                "name": "Tag 3",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                            {
                                "id": "tag4",
                                "remote_id": None,
                                "name": "Tag 4",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": "cursor_page3",
                    },
                },
            },
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag5",
                                "remote_id": None,
                                "name": "Tag 5",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": None,
                    },
                },
            },
        )

        page = ctx.kombo.ats.get_tags()
        all_results = []

        # Iterate through all pages
        while page is not None:
            all_results.extend(page.result.data.results)
            page = page.next()

        # Verify all 5 tags were collected
        assert len(all_results) == 5
        assert [tag.id for tag in all_results] == ["tag1", "tag2", "tag3", "tag4", "tag5"]

        # Verify 3 HTTP requests were made
        requests = ctx.get_requests()
        assert len(requests) == 3

    def test_should_pass_cursor_parameter_to_subsequent_requests(self):
        """Test that cursor parameter is passed to subsequent paginated requests."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag1",
                                "remote_id": None,
                                "name": "Tag 1",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": "test_cursor_abc123",
                    },
                },
            },
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag2",
                                "remote_id": None,
                                "name": "Tag 2",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": None,
                    },
                },
            },
        )

        page = ctx.kombo.ats.get_tags()
        # Iterate through all pages
        while page is not None:
            page = page.next()

        requests = ctx.get_requests()
        assert len(requests) == 2

        # First request should NOT include cursor
        assert "cursor=" not in requests[0].path

        # Second request SHOULD include cursor
        assert "cursor=test_cursor_abc123" in requests[1].path

    def test_should_stop_pagination_when_next_is_null(self):
        """Test that pagination stops when next cursor is null."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag1",
                                "remote_id": None,
                                "name": "Tag 1",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                            {
                                "id": "tag2",
                                "remote_id": None,
                                "name": "Tag 2",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": None,
                    },
                },
            },
        )

        page = ctx.kombo.ats.get_tags()
        page_count = []

        while page is not None:
            page_count.append(1)
            page = page.next()

        # Verify only 1 page was returned
        assert len(page_count) == 1

        # Verify only 1 HTTP request was made
        requests = ctx.get_requests()
        assert len(requests) == 1

    def test_should_preserve_query_parameters_across_paginated_requests(self):
        """Test that original query parameters are preserved across paginated requests."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag1",
                                "remote_id": None,
                                "name": "Tag 1",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": "cursor_for_page2",
                    },
                },
            },
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag2",
                                "remote_id": None,
                                "name": "Tag 2",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": None,
                    },
                },
            },
        )

        page = ctx.kombo.ats.get_tags(
            updated_after=datetime(2024, 1, 1, 0, 0, 0)
        )

        # Iterate through all pages
        while page is not None:
            page = page.next()

        requests = ctx.get_requests()
        assert len(requests) == 2

        # Both requests should include the original query parameters
        # Check that updated_after parameter is present (URL encoded)
        assert "updated_after=2024-01-01T00%3A00%3A00" in requests[0].path
        assert "cursor=" not in requests[0].path

        assert "updated_after=2024-01-01T00%3A00%3A00" in requests[1].path
        assert "cursor=cursor_for_page2" in requests[1].path

    def test_should_support_manual_pagination_with_next(self):
        """Test that manual pagination works by calling next() method."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag1",
                                "remote_id": None,
                                "name": "Tag 1",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": "manual_cursor_xyz",
                    },
                },
            },
        )

        ctx.mock_endpoint(
            method="GET",
            path="/v1/ats/tags",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "results": [
                            {
                                "id": "tag2",
                                "remote_id": None,
                                "name": "Tag 2",
                                "changed_at": "2024-01-01T00:00:00.000Z",
                                "remote_deleted_at": None,
                            },
                        ],
                        "next": None,
                    },
                },
            },
        )

        page1 = ctx.kombo.ats.get_tags()

        # Verify first page was fetched
        assert page1.result.data.results is not None
        assert len(page1.result.data.results) == 1

        # Manually call next()
        page2_result = page1.next()

        # Verify second page was fetched (should not be null if cursor was read correctly)
        # This will fail if cursor extraction bug exists
        assert page2_result is not None
        if page2_result:
            assert len(page2_result.result.data.results) == 1
            assert page2_result.result.data.results[0].id == "tag2"

        # Verify 2 HTTP requests were made
        requests = ctx.get_requests()
        assert len(requests) == 2
        assert "cursor=manual_cursor_xyz" in requests[1].path

