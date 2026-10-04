# PaidAmountYtd

The year-to-date paid amount as returned by the remote system. Kombo never calculates this value. `null` when the remote API does not provide a year-to-date amount.


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `currency`                                                                                                  | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The [ISO 4217 currency code](https://www.iso.org/iso-4217-currency-codes.html) the value is denominated in. |
| `value`                                                                                                     | *float*                                                                                                     | :heavy_check_mark:                                                                                          | The monetary value.                                                                                         |