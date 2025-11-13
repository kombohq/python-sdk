# ~~PostAtsCandidatesRequestBodySource~~

**(⚠️ Deprecated - Use [automatic source writing](/ats/features/application-attribution#automatic-attribution) instead)** Optional source information that will be attached to the candidate. If
you're a job board or recruiting service, you can use this to make sure your
customers can see which candidates came from you.

This is deprecated because writing sources requires users to do some setup in most ATSs.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `name`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | Name of the source (e.g., `"Example Job Board"`). |
| `unified_key`                                     | *Optional[str]*                                   | :heavy_minus_sign:                                | N/A                                               |
| `id`                                              | *Optional[str]*                                   | :heavy_minus_sign:                                | N/A                                               |