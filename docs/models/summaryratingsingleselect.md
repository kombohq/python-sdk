# SummaryRatingSingleSelect


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `type`                                                       | *Literal["SINGLE_SELECT"]*                                   | :heavy_check_mark:                                           | N/A                                                          |
| `ordered_options`                                            | List[*str*]                                                  | :heavy_check_mark:                                           | The options of the summary rating. Ordered from bad to good. |
| `value`                                                      | *Nullable[str]*                                              | :heavy_check_mark:                                           | The text value of the summary rating.                        |