# KomboGeneralErrorCode

Some errors include an error code that can be used to identify their cause. See the [Error Handling Docs](https://docs.kombo.dev/guides/errors) for more information. For your error handling logic please use the error `code` instead of other properties (e.g. message, http status code, ...).

## Example Usage

```python
from kombo.models import KomboGeneralErrorCode
value: KomboGeneralErrorCode = "PLATFORM.RATE_LIMIT_EXCEEDED"
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
