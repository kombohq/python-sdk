# RemoteWorkStatus

## Example Usage

```python
from kombo.models import RemoteWorkStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RemoteWorkStatus = "REMOTE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"REMOTE"`
- `"HYBRID"`
- `"TEMPORARY"`
- `"ON_SITE"`
