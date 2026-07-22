# ExpectedProficiencySingleSelect


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `type`                                                                                       | *Literal["SINGLE_SELECT"]*                                                                   | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `selected_option_id`                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The Kombo ID of the selected option on the scale (`proficiency_scale.ordered_options[].id`). |