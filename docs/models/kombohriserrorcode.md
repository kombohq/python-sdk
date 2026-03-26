# KomboHrisErrorCode

Some errors include an error code that can be used to identify their cause. See the [Error Handling Docs](https://docs.kombo.dev/guides/errors) for more information. For your error handling logic please use the error `code` instead of other properties (e.g. message, http status code, ...).

## Example Usage

```python
from kombo.models import KomboHrisErrorCode
value: KomboHrisErrorCode = "PLATFORM.RATE_LIMIT_EXCEEDED"
```


## Values

- `"PLATFORM.RATE_LIMIT_EXCEEDED"`
- `"PLATFORM.CONCURRENCY_LIMIT_EXCEEDED"`
- `"PLATFORM.INTEGRATION_NOT_FOUND"`
- `"PLATFORM.INPUT_INVALID"`
- `"PLATFORM.UNKNOWN_ERROR"`
- `"PLATFORM.IP_NOT_WHITELISTED"`
- `"PLATFORM.AUTHENTICATION_INVALID"`
- `"PLATFORM.TASK_TIMED_OUT"`
- `"INTEGRATION.PERMISSION_MISSING"`
- `"INTEGRATION.AUTHENTICATION_INVALID"`
- `"INTEGRATION.QA_FAILED"`
- `"INTEGRATION.SETUP_SYNC_PENDING"`
- `"INTEGRATION.SETUP_INCOMPLETE"`
- `"INTEGRATION.INACTIVE"`
- `"INTEGRATION.MODEL_NOT_AVAILABLE"`
- `"INTEGRATION.MODEL_DISABLED"`
- `"INTEGRATION.ACTION_NOT_AVAILABLE"`
- `"INTEGRATION.ACTION_DISABLED"`
- `"REMOTE.SERVICE_UNAVAILABLE"`
- `"REMOTE.RATE_LIMIT_EXCEEDED"`
- `"REMOTE.INPUT_INVALID"`
- `"REMOTE.UNKNOWN_HTTP_ERROR"`
- `"HRIS.EMPLOYEE_ALREADY_EXISTS"`
