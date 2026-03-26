# PostForceSyncPositiveResponseType

The type of the triggered sync. May differ from request, if the integration does not support delta syncs or if another sync is already running.

## Example Usage

```python
from kombo.models import PostForceSyncPositiveResponseType
value: PostForceSyncPositiveResponseType = "FULL"
```


## Values

- `"FULL"`
- `"DELTA"`
