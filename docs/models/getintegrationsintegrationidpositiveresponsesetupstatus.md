# GetIntegrationsIntegrationIDPositiveResponseSetupStatus

The setup_status is used in conjunction with the filtering and field mapping features. If these are enabled in the connection flow, the integration will start in an "INCOMPLETE" state and move to "COMPLETE" once all steps are finished.

- `INCOMPLETE`: Setup is still in progress. Some steps aren’t finished, so no data is available yet. Syncs only run as needed for setup.
- `FINAL_SYNC_PENDING`: Setup is complete, and the final sync is running. Data will be available after this sync is done.
- `COMPLETED`: Setup is fully finished, and the integration is ready to use.

## Example Usage

```python
from kombo.models import GetIntegrationsIntegrationIDPositiveResponseSetupStatus
value: GetIntegrationsIntegrationIDPositiveResponseSetupStatus = "INCOMPLETE"
```


## Values

- `"INCOMPLETE"`
- `"FINAL_SYNC_PENDING"`
- `"COMPLETED"`
