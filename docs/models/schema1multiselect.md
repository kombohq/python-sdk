# Schema1MultiSelect


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `label`                                                          | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `required`                                                       | *bool*                                                           | :heavy_check_mark:                                               | N/A                                                              |
| `description`                                                    | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `unified_key`                                                    | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `type`                                                           | *Literal["multi_select"]*                                        | :heavy_check_mark:                                               | N/A                                                              |
| `min_items`                                                      | *OptionalNullable[float]*                                        | :heavy_minus_sign:                                               | N/A                                                              |
| `max_items`                                                      | *OptionalNullable[float]*                                        | :heavy_minus_sign:                                               | N/A                                                              |
| `options`                                                        | [models.Schema1OptionsUnion2](../models/schema1optionsunion2.md) | :heavy_check_mark:                                               | N/A                                                              |