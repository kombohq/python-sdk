# GetAssessmentOrdersPositiveResponseCandidate

Information about the candidate taking the assessment.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `remote_id`                                          | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's identifier in the integrated system. | 12345                                                |
| `email`                                              | *str*                                                | :heavy_check_mark:                                   | The candidate's email address.                       | john.doe@gmail.com                                   |
| `first_name`                                         | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's first name.                          | John                                                 |
| `last_name`                                          | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's last name.                           | Doe                                                  |
| `phone`                                              | *Nullable[str]*                                      | :heavy_check_mark:                                   | The candidate's phone number.                        | +1 123 456 7890                                      |