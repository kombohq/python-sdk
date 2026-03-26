# ModelType

The remote model type of the record. Possible values are "JOB", "POSITION" or "REQUISITION". We recommend that users of our `create employee` endpoint ask the customer whether they want to hire into positions or requisitions.

## Example Usage

```python
from kombo.models import ModelType
value: ModelType = "JOB"
```


## Values

- `"JOB"`
- `"POSITION"`
- `"REQUISITION"`
