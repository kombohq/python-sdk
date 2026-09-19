# ContentRef


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `type`                                                                        | *Literal["s3"]*                                                               | :heavy_check_mark:                                                            | N/A                                                                           |
| `bucket`                                                                      | *str*                                                                         | :heavy_check_mark:                                                            | The bucket the object was written to.                                         |
| `key`                                                                         | *str*                                                                         | :heavy_check_mark:                                                            | The full object key, including the prefix configured on the file destination. |