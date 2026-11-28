# KomboPassthroughError

The standard error response with the error codes for the passthrough API.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `status`                                                                       | [models.KomboPassthroughErrorStatus](../models/kombopassthrougherrorstatus.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `error`                                                                        | [models.KomboPassthroughErrorError](../models/kombopassthrougherrorerror.md)   | :heavy_check_mark:                                                             | Error details with structured code for programmatic handling.                  |