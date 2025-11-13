# KomboGeneralErrorCode

Some errors include an error code that can be used to identify their cause. See the [Error Handling Docs](https://docs.kombo.dev/guides/errors) for more information. For your error handling logic please use the error `code` instead of other properties (e.g. message, http status code, ...).


## Values

| Name                              | Value                             |
| --------------------------------- | --------------------------------- |
| `PLATFORM_RATE_LIMIT_EXCEEDED`    | PLATFORM.RATE_LIMIT_EXCEEDED      |
| `PLATFORM_INTEGRATION_NOT_FOUND`  | PLATFORM.INTEGRATION_NOT_FOUND    |
| `PLATFORM_INPUT_INVALID`          | PLATFORM.INPUT_INVALID            |
| `PLATFORM_UNKNOWN_ERROR`          | PLATFORM.UNKNOWN_ERROR            |
| `PLATFORM_IP_NOT_WHITELISTED`     | PLATFORM.IP_NOT_WHITELISTED       |
| `PLATFORM_AUTHENTICATION_INVALID` | PLATFORM.AUTHENTICATION_INVALID   |