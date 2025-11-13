# KomboHrisError

The standard error response with the error codes for the HRIS use case.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `status`                                                         | [models.KomboHrisErrorStatus](../models/kombohriserrorstatus.md) | :heavy_check_mark:                                               | N/A                                                              |
| `error`                                                          | [models.KomboHrisErrorError](../models/kombohriserrorerror.md)   | :heavy_check_mark:                                               | Error details with structured code for programmatic handling.    |