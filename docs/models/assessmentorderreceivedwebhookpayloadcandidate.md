# AssessmentOrderReceivedWebhookPayloadCandidate

Information about the candidate taking the assessment.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `remote_id`                                          | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's identifier in the integrated system. |
| `email`                                              | *str*                                                | :heavy_check_mark:                                   | The candidate's email address.                       |
| `first_name`                                         | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's first name.                          |
| `last_name`                                          | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's last name.                           |
| `phone`                                              | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's phone number.                        |