# IssueStatusChangedWebhookPayloadData


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `change`                                                                   | [models.Change](../models/change.md)                                       | :heavy_check_mark:                                                         | Why this webhook was sent: the issue was raised or resolved.               |
| `issue`                                                                    | [models.Issue](../models/issue.md)                                         | :heavy_check_mark:                                                         | N/A                                                                        |
| `integration`                                                              | [Nullable[models.Integration]](../models/integration.md)                   | :heavy_check_mark:                                                         | The integration this issue belongs to. `null` for environment-wide issues. |