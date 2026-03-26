# Visibility

## Example Usage

```python
from kombo.models import Visibility

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Visibility = "PUBLIC"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PUBLIC"`
- `"INTERNAL"`
- `"UNLISTED"`
- `"CONFIDENTIAL"`
