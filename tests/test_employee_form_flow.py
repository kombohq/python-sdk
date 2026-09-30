"""Tests for employee form flow endpoints."""

from inline_snapshot import snapshot
from tests.conftest import MockContext


class TestEmployeeFormFlow:
    """Test employee form flow endpoints."""

    def test_get_employee_form(self):
        """Test that get_employee_form() works correctly and returns a form response."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="GET",
            path="/v1/hris/employees/form",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "properties": {
                            "firstName": {
                                "type": "text",
                                "label": "First Name",
                                "required": True,
                                "description": "Employee's first name",
                                "unified_key": "first_name",
                                "min_length": 1,
                                "max_length": 100,
                            },
                            "lastName": {
                                "type": "text",
                                "label": "Last Name",
                                "required": True,
                                "description": "Employee's last name",
                                "unified_key": "last_name",
                                "min_length": 1,
                                "max_length": 100,
                            },
                            "startDate": {
                                "type": "date",
                                "label": "Start Date",
                                "required": True,
                                "description": "Employee's start date",
                                "unified_key": "start_date",
                            },
                            "keyNumbers": {
                                "type": "array",
                                "label": "Key Numbers",
                                "required": False,
                                "description": "Employee's key numbers",
                                "unified_key": None,
                                "min_items": 2,
                                "max_items": 5,
                                "item_type": {
                                    "type": "number",
                                    "label": "Key Number",
                                    "required": False,
                                    "description": "The number of the keys which belong to the employee",
                                    "unified_key": None,
                                    "min": 0,
                                    "max": 99,
                                },
                            },
                            "workLocation": {
                                "type": "object",
                                "label": "Work Location",
                                "required": False,
                                "description": "Employee's work location",
                                "unified_key": None,
                                "properties": {
                                    "site": {
                                        "type": "single_select",
                                        "label": "Site",
                                        "required": True,
                                        "description": "Employee's site",
                                        "unified_key": None,
                                        "options": {
                                            "type": "inline",
                                            "entries": [
                                                {
                                                    "label": "Site 1",
                                                    "id": "FXrER44xubBqA9DLgZ3PFNNx",
                                                    "unified_value": "1",
                                                    "remote_id": "site_1",
                                                },
                                                {
                                                    "label": "Site 2",
                                                    "id": "2rv75UKT2XBoQXsUb9agiTUm",
                                                    "unified_value": "2",
                                                    "remote_id": "site_2",
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "warnings": [],
                },
            },
        )

        # Make the API call
        form = ctx.kombo.hris.get_employee_form()

        # Verify the response structure
        assert form is not None
        assert form.status == "success"
        assert form.data is not None
        assert "firstName" in form.data.properties
        assert "keyNumbers" in form.data.properties
        assert form.warnings == []

    def test_create_employee_with_form(self):
        """Test that create_employee_with_form() works correctly with realistic employee data."""
        ctx = MockContext()

        ctx.mock_endpoint(
            method="POST",
            path="/v1/hris/employees/form",
            response={
                "body": {
                    "status": "success",
                    "data": {
                        "id": "emp-123",
                        "remote_id": "remote-emp-123",
                        "prehire": {
                            "remote_id": None,
                        },
                    },
                    "warnings": [],
                },
            },
        )

        # Make the API call with realistic employee properties
        result = ctx.kombo.hris.create_employee_with_form(
            properties={
                "firstName": "John",
                "lastName": "Doe",
                "startDate": "2025-01-15",
                "keyNumbers": [142, 525, 63],
                "workLocation": {
                    "site": "FXrER44xubBqA9DLgZ3PFNNx",
                },
            }
        )

        # Verify the response structure
        assert result is not None
        assert result.status == "success"
        assert result.data is not None
        assert result.data.id == "emp-123"
        assert result.data.remote_id == "remote-emp-123"
        assert result.warnings == []

        # Verify request body is correctly serialized
        request = ctx.get_last_request()
        assert request.method == "POST"
        assert request.body == snapshot(
            {
                "properties": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "startDate": "2025-01-15",
                    "keyNumbers": [142, 525, 63],
                    "workLocation": {
                        "site": "FXrER44xubBqA9DLgZ3PFNNx",
                    },
                }
            }
        )

