# InlineAssessmentOrderReceivedWebhookPayloadCandidate

Information about the candidate taking the assessment.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `email`                                              | *str*                                                | :heavy_check_mark:                                   | The candidate's email address.                       |
| `first_name`                                         | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | The candidate's first name.                          |
| `last_name`                                          | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | The candidate's last name.                           |
| `phone`                                              | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | The candidate's phone number.                        |
| `remote_id`                                          | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | The candidate's identifier in the integrated system. |