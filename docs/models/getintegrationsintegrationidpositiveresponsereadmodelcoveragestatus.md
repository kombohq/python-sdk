# GetIntegrationsIntegrationIDPositiveResponseReadModelCoverageStatus

The status of a datapoint of an integrated tool:

- `SUPPORTED`: the tool supports the datapoint and it can be used through Kombo.
- `UNSUPPORTED`: the tool does not support the datapoint.
- `NOT_IMPLEMENTED`: tool supports the datapoint but it was not integrated by Kombo for a given reason (see coverage grid).
- `UNKNOWN`: the datapoint is not integrated yet and Kombo has no information about it's availability in the tool.

## Example Usage

```python
from kombo.models import GetIntegrationsIntegrationIDPositiveResponseReadModelCoverageStatus
value: GetIntegrationsIntegrationIDPositiveResponseReadModelCoverageStatus = "SUPPORTED"
```


## Values

- `"SUPPORTED"`
- `"UNSUPPORTED"`
- `"NOT_IMPLEMENTED"`
- `"UNKNOWN"`
