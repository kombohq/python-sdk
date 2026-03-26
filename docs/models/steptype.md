# StepType

The type of step reference to use. Use "Next_Step_Reference" for regular stage moves and "Disposition_Step_Reference" for conclusion/disposition stages (e.g., rejected, declined). Defaults to "Next_Step_Reference".

## Example Usage

```python
from kombo.models import StepType
value: StepType = "Next_Step_Reference"
```


## Values

- `"Next_Step_Reference"`
- `"Disposition_Step_Reference"`
