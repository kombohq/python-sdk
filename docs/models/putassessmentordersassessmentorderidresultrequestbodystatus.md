# PutAssessmentOrdersAssessmentOrderIDResultRequestBodyStatus

Status of the assessment.

**Please note the `status` can only be updated to a different value if its current value is `OPEN`.**

## Example Usage

```python
from kombo.models import PutAssessmentOrdersAssessmentOrderIDResultRequestBodyStatus
value: PutAssessmentOrdersAssessmentOrderIDResultRequestBodyStatus = "COMPLETED"
```


## Values

- `"COMPLETED"`
- `"CANCELLED"`
- `"OPEN"`
