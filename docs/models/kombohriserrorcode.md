# KomboHrisErrorCode

Some errors include an error code that can be used to identify their cause. See the [Error Handling Docs](https://docs.kombo.dev/guides/errors) for more information. For your error handling logic please use the error `code` instead of other properties (e.g. message, http status code, ...).


## Values

| Name                                 | Value                                |
| ------------------------------------ | ------------------------------------ |
| `PLATFORM_RATE_LIMIT_EXCEEDED`       | PLATFORM.RATE_LIMIT_EXCEEDED         |
| `PLATFORM_INTEGRATION_NOT_FOUND`     | PLATFORM.INTEGRATION_NOT_FOUND       |
| `PLATFORM_INPUT_INVALID`             | PLATFORM.INPUT_INVALID               |
| `PLATFORM_UNKNOWN_ERROR`             | PLATFORM.UNKNOWN_ERROR               |
| `PLATFORM_IP_NOT_WHITELISTED`        | PLATFORM.IP_NOT_WHITELISTED          |
| `PLATFORM_AUTHENTICATION_INVALID`    | PLATFORM.AUTHENTICATION_INVALID      |
| `PLATFORM_TASK_TIMED_OUT`            | PLATFORM.TASK_TIMED_OUT              |
| `INTEGRATION_PERMISSION_MISSING`     | INTEGRATION.PERMISSION_MISSING       |
| `INTEGRATION_AUTHENTICATION_INVALID` | INTEGRATION.AUTHENTICATION_INVALID   |
| `INTEGRATION_QA_FAILED`              | INTEGRATION.QA_FAILED                |
| `INTEGRATION_SETUP_SYNC_PENDING`     | INTEGRATION.SETUP_SYNC_PENDING       |
| `INTEGRATION_SETUP_INCOMPLETE`       | INTEGRATION.SETUP_INCOMPLETE         |
| `INTEGRATION_INACTIVE`               | INTEGRATION.INACTIVE                 |
| `INTEGRATION_MODEL_NOT_AVAILABLE`    | INTEGRATION.MODEL_NOT_AVAILABLE      |
| `INTEGRATION_MODEL_DISABLED`         | INTEGRATION.MODEL_DISABLED           |
| `INTEGRATION_ACTION_NOT_AVAILABLE`   | INTEGRATION.ACTION_NOT_AVAILABLE     |
| `INTEGRATION_ACTION_DISABLED`        | INTEGRATION.ACTION_DISABLED          |
| `REMOTE_SERVICE_UNAVAILABLE`         | REMOTE.SERVICE_UNAVAILABLE           |
| `REMOTE_RATE_LIMIT_EXCEEDED`         | REMOTE.RATE_LIMIT_EXCEEDED           |
| `REMOTE_INPUT_INVALID`               | REMOTE.INPUT_INVALID                 |
| `REMOTE_UNKNOWN_HTTP_ERROR`          | REMOTE.UNKNOWN_HTTP_ERROR            |
| `HRIS_EMPLOYEE_ALREADY_EXISTS`       | HRIS.EMPLOYEE_ALREADY_EXISTS         |