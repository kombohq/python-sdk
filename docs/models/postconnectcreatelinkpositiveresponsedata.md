# PostConnectCreateLinkPositiveResponseData


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `link`                                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `static_ips`                                                                        | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | The allowlist IPs for this integration. Present when `enable_static_ips` is `true`. |