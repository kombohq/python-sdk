# GetAtsApplicationsPositiveResponseStatus

The offer’s current status. The usual flow of statuses is as follows:
`DRAFT` -> `APPROVED` -> `SENT` -> `ACCEPTED` or `DECLINED`.

Please note that not all systems will expose all statuses. For example, most systems do not include the `APPROVED` status

- `ACCEPTED`: The offer was accepted by the candidate.
- `DECLINED`: The offer was declined by the candidate.
- `SENT`: The offer was sent to the candidate.
- `APPROVED`: The draft was approved.
- `DRAFT`: The offer is a draft and has not yet been sent to the candidate.
- `ABANDONED`: The offer has expired or is no longer valid and should not be considered.



## Values

| Name        | Value       |
| ----------- | ----------- |
| `ACCEPTED`  | ACCEPTED    |
| `DECLINED`  | DECLINED    |
| `SENT`      | SENT        |
| `APPROVED`  | APPROVED    |
| `DRAFT`     | DRAFT       |
| `ABANDONED` | ABANDONED   |