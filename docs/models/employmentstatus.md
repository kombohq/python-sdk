# EmploymentStatus

## Example Usage

```python
from kombo.models import EmploymentStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EmploymentStatus = "ACTIVE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ACTIVE"`
- `"PENDING"`
- `"INACTIVE"`
- `"LEAVE"`
