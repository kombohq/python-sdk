<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.check_api_key()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from kombo import Kombo

async def main():

    async with Kombo(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as k_client:

        res = await k_client.general.check_api_key_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->