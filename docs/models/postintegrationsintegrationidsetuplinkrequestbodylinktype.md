# PostIntegrationsIntegrationIDSetupLinkRequestBodyLinkType

The type of link you want to create. `EMBEDDED` is for the [embedded flow](../guides/connect/embedded-flow) using the Kombo Connect SDK (these links are valid for 1 hour) and `MAGIC_LINK` is for [magic links](../guides/connect/magic-links) which you send out manually to customers (these are valid for 1 year).

## Example Usage

```python
from kombo.models import PostIntegrationsIntegrationIDSetupLinkRequestBodyLinkType
value: PostIntegrationsIntegrationIDSetupLinkRequestBodyLinkType = "EMBEDDED"
```


## Values

- `"EMBEDDED"`
- `"MAGIC_LINK"`
