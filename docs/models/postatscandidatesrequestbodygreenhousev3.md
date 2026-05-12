# PostAtsCandidatesRequestBodyGreenhousev3

Fields specific to Greenhouse V3 (OAuth-based connector).


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `candidate`                                                                               | Dict[str, *Any*]                                                                          | :heavy_minus_sign:                                                                        | Additional fields passed through to Greenhouse V3's `POST /v3/candidates` request body.   |
| `application`                                                                             | Dict[str, *Any*]                                                                          | :heavy_minus_sign:                                                                        | Additional fields passed through to Greenhouse V3's `POST /v3/applications` request body. |