# KomboAtsError

The standard error response with the error codes for the ATS use case.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `status`                                                       | [models.KomboAtsErrorStatus](../models/komboatserrorstatus.md) | :heavy_check_mark:                                             | N/A                                                            |
| `error`                                                        | [models.KomboAtsErrorError](../models/komboatserrorerror.md)   | :heavy_check_mark:                                             | Error details with structured code for programmatic handling.  |