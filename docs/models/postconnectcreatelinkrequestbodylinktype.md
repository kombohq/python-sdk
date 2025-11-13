# PostConnectCreateLinkRequestBodyLinkType

The type of link you want to create. `EMBEDDED` is for the [embedded flow](../guides/connect/embedded-flow) using the Kombo Connect SDK (these links are valid for 1 hour) and `MAGIC_LINK` is for [magic links](../guides/connect/magic-links) which you send out manually to customers (there are valid for 1 year).

This defaults to `EMBEDDED`, which is our recommended method of implementing the connection flow for a seamless user experience.


## Values

| Name         | Value        |
| ------------ | ------------ |
| `EMBEDDED`   | EMBEDDED     |
| `MAGIC_LINK` | MAGIC_LINK   |