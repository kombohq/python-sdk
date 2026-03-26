# GetHrisStaffingEntitiesPositiveResponseStatus

The status of the staffing entity.
        OPEN_LIMITED: The staffing entity is open and has a limited number of openings. Refer to the `number_of_openings` field to get the number of openings.
        OPEN_UNLIMITED: The staffing entity is open and has an unlimited number of openings. Some enterprise systems refer to this as "Evergreen".
        PENDING: The staffing entity is pending approval or is waiting to be published.
        FROZEN: The staffing entity is frozen (hiring freeze) and does not accept applications/hires.
        FILLED: The staffing entity is filled (to its maximum capacity) and not available for new hires.
        CLOSED: The staffing entity is closed and not available for new hires.

## Example Usage

```python
from kombo.models import GetHrisStaffingEntitiesPositiveResponseStatus
value: GetHrisStaffingEntitiesPositiveResponseStatus = "OPEN_LIMITED"
```


## Values

- `"OPEN_LIMITED"`
- `"OPEN_UNLIMITED"`
- `"PENDING"`
- `"FROZEN"`
- `"FILLED"`
- `"CLOSED"`
