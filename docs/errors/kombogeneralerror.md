# KomboGeneralError

The standard error response with just the platform error codes.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `status`                                                               | [models.KomboGeneralErrorStatus](../models/kombogeneralerrorstatus.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `error`                                                                | [models.KomboGeneralErrorError](../models/kombogeneralerrorerror.md)   | :heavy_check_mark:                                                     | Error details with structured code for programmatic handling.          |