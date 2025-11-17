# openapi

Developer-friendly & type-safe Python SDK specifically catered to leverage *openapi* API.

<div align="left" style="margin-bottom: 0;">
    <a href="https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python" class="badge-link">
        <span class="badge-container">
            <span class="badge-icon-section">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 30 30" fill="none" style="vertical-align: middle;"><title>Speakeasy Logo</title><path fill="currentColor" d="m20.639 27.548-19.17-2.724L0 26.1l20.639 2.931 8.456-7.336-1.468-.208-6.988 6.062Z"></path><path fill="currentColor" d="m20.639 23.1 8.456-7.336-1.468-.207-6.988 6.06-6.84-.972-9.394-1.333-2.936-.417L0 20.169l2.937.416L0 23.132l20.639 2.931 8.456-7.334-1.468-.208-6.986 6.062-9.78-1.39 1.468-1.273 8.31 1.18Z"></path><path fill="currentColor" d="m20.639 18.65-19.17-2.724L0 17.201l20.639 2.931 8.456-7.334-1.468-.208-6.988 6.06Z"></path><path fill="currentColor" d="M27.627 6.658 24.69 9.205 20.64 12.72l-7.923-1.126L1.469 9.996 0 11.271l11.246 1.596-1.467 1.275-8.311-1.181L0 14.235l20.639 2.932 8.456-7.334-2.937-.418 2.937-2.549-1.468-.208Z"></path><path fill="currentColor" d="M29.095 3.902 8.456.971 0 8.305l20.639 2.934 8.456-7.337Z"></path></svg>
            </span>
            <span class="badge-text badge-text-section">BUILT BY SPEAKEASY</span>
        </span>
    </a>
    <a href="https://opensource.org/licenses/MIT" class="badge-link">
        <span class="badge-container blue">
            <span class="badge-text badge-text-section">LICENSE // MIT</span>
        </span>
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/kombo-ayg/api). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [openapi](https://github.com/kombohq/python-sdk/blob/master/#openapi)
  * [SDK Installation](https://github.com/kombohq/python-sdk/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/kombohq/python-sdk/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/kombohq/python-sdk/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/kombohq/python-sdk/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/kombohq/python-sdk/blob/master/#available-resources-and-operations)
  * [Global Parameters](https://github.com/kombohq/python-sdk/blob/master/#global-parameters)
  * [Pagination](https://github.com/kombohq/python-sdk/blob/master/#pagination)
  * [Retries](https://github.com/kombohq/python-sdk/blob/master/#retries)
  * [Error Handling](https://github.com/kombohq/python-sdk/blob/master/#error-handling)
  * [Server Selection](https://github.com/kombohq/python-sdk/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/kombohq/python-sdk/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/kombohq/python-sdk/blob/master/#resource-management)
  * [Debugging](https://github.com/kombohq/python-sdk/blob/master/#debugging)
* [Development](https://github.com/kombohq/python-sdk/blob/master/#development)
  * [Maturity](https://github.com/kombohq/python-sdk/blob/master/#maturity)
  * [Contributions](https://github.com/kombohq/python-sdk/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add kombo-python
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install kombo-python
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add kombo-python
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from kombo-python python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "kombo-python",
# ]
# ///

from kombo_python import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from kombo_python import SDK


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from kombo_python import SDK

async def main():

    async with SDK(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:

        res = await sdk.general.check_api_key_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      |
| --------- | ---- | ----------- |
| `api_key` | http | HTTP Bearer |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from kombo_python import SDK


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [assessment](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/assessment/README.md)

* [get_packages](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/assessment/README.md#get_packages) - Get packages
* [set_packages](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/assessment/README.md#set_packages) - Set packages
* [get_open_orders](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/assessment/README.md#get_open_orders) - Get open orders
* [update_order_result](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/assessment/README.md#update_order_result) - Update order result

### [ats](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md)

* [get_applications](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_applications) - Get applications
* [move_application_to_stage](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#move_application_to_stage) - Move application to stage
* [add_application_result_link](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#add_application_result_link) - Add result link to application
* [add_application_note](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#add_application_note) - Add note to application
* [get_application_attachments](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_application_attachments) - Get application attachments
* [add_application_attachment](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#add_application_attachment) - Add attachment to application
* [reject_application](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#reject_application) - Reject application
* [get_candidates](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_candidates) - Get candidates
* [create_candidate](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#create_candidate) - Create candidate
* [get_candidate_attachments](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_candidate_attachments) - Get candidate attachments
* [add_candidate_attachment](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#add_candidate_attachment) - Add attachment to candidate
* [add_candidate_result_link](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#add_candidate_result_link) - Add result link to candidate
* [add_candidate_tag](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#add_candidate_tag) - Add tag to candidate
* [remove_candidate_tag](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#remove_candidate_tag) - Remove tag from candidate
* [get_tags](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_tags) - Get tags
* [get_application_stages](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_application_stages) - Get application stages
* [get_jobs](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_jobs) - Get jobs
* [create_application](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#create_application) - Create application
* [get_users](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_users) - Get users
* [get_offers](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_offers) - Get offers
* [get_rejection_reasons](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_rejection_reasons) - Get rejection reasons
* [get_interviews](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#get_interviews) - Get interviews
* [import_tracked_application](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/ats/README.md#import_tracked_application) - Import tracked application

### [connect](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/connect/README.md)

* [create_connection_link](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/connect/README.md#create_connection_link) - Create connection link
* [get_integration_by_token](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/connect/README.md#get_integration_by_token) - Get integration by token

### [general](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md)

* [check_api_key](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#check_api_key) - Check API key
* [trigger_sync](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#trigger_sync) - Trigger sync
* [send_passthrough_request](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#send_passthrough_request) - Send passthrough request
* [delete_integration](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#delete_integration) - Delete integration
* [get_integration_details](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#get_integration_details) - Get integration details
* [create_reconnection_link](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#create_reconnection_link) - Create reconnection link
* [get_integration_fields](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#get_integration_fields) - Get integration fields
* [update_integration_field](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#update_integration_field) - Updates an integration fields passthrough setting
* [get_custom_fields](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#get_custom_fields) - Get custom fields with current mappings
* [update_custom_field_mapping](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#update_custom_field_mapping) - Put custom field mappings
* [get_tools](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/general/README.md#get_tools) - Get tools

### [hris](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md)

* [get_employees](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_employees) - Get employees
* [get_employee_form](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_employee_form) - Get employee form
* [create_employee_with_form](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#create_employee_with_form) - Create employee with form
* [add_employee_document](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#add_employee_document) - Add document to employee
* [get_employee_document_categories](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_employee_document_categories) - Get employee document categories
* [get_groups](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_groups) - Get groups
* [get_employments](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_employments) - Get employments
* [get_locations](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_locations) - Get work locations
* [get_absence_types](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_absence_types) - Get absence types
* [get_time_off_balances](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_time_off_balances) - Get time off balances
* [get_absences](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_absences) - Get absences
* [create_absence](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#create_absence) - Create absence
* [delete_absence](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#delete_absence) - Delete absence
* [get_legal_entities](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_legal_entities) - Get legal entities
* [get_timesheets](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_timesheets) - Get timesheets
* [get_performance_review_cycles](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_performance_review_cycles) - Get performance review cycles
* [get_performance_reviews](https://github.com/kombohq/python-sdk/blob/master/docs/sdks/hris/README.md#get_performance_reviews) - Get performance reviews

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `integration_id` to `"workday:HWUTwvyx2wLoSUHphiWVrp28"` at SDK initialization and then you do not have to pass the same value on calls to operations like `delete_integration`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.

| Name           | Type | Description                                      |
| -------------- | ---- | ------------------------------------------------ |
| integration_id | str  | ID of the integration you want to interact with. |

### Example

```python
from kombo_python import SDK


with SDK(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.delete_integration(integration_id="<id>", body={})

    # Handle response
    print(res)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from kombo_python import SDK


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.get_integration_fields(integration_id="<id>", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from kombo_python import SDK
from kombo_python.utils import BackoffStrategy, RetryConfig


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from kombo_python import SDK
from kombo_python.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/sdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/kombohq/python-sdk/blob/master/#error-classes). |

### Example
```python
from kombo_python import SDK, errors


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:
    res = None
    try:

        res = sdk.general.check_api_key()

        # Handle response
        print(res)


    except errors.SDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.KomboGeneralError):
            print(e.data.status)  # models.KomboGeneralErrorStatus
            print(e.data.error)  # models.KomboGeneralErrorError
```

### Error Classes
**Primary error:**
* [`SDKError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/sdkerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (8)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/sdkerror.py)**:
* [`KomboAtsError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/komboatserror.py): The standard error response with the error codes for the ATS use case. Applicable to 27 of 57 methods.*
* [`KomboHrisError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/kombohriserror.py): The standard error response with the error codes for the HRIS use case. Applicable to 17 of 57 methods.*
* [`KomboGeneralError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/kombogeneralerror.py): The standard error response with just the platform error codes. Applicable to 13 of 57 methods.*
* [`ResponseValidationError`](https://github.com/kombohq/python-sdk/blob/master/./src/kombo_python/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/kombohq/python-sdk/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server                        | Description     |
| ---- | ----------------------------- | --------------- |
| `eu` | `https://api.kombo.dev/v1`    | Kombo EU Region |
| `us` | `https://api.us.kombo.dev/v1` | Kombo US Region |

#### Example

```python
from kombo_python import SDK


with SDK(
    server="eu",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from kombo_python import SDK


with SDK(
    server_url="https://api.kombo.dev/v1",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from kombo_python import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from kombo_python import SDK
from kombo_python.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from kombo_python import SDK
def main():

    with SDK(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from kombo_python import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("kombo_python"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)

<style>
  :root {
    --badge-gray-bg: #f3f4f6;
    --badge-gray-border: #d1d5db;
    --badge-gray-text: #374151;
    --badge-blue-bg: #eff6ff;
    --badge-blue-border: #3b82f6;
    --badge-blue-text: #3b82f6;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --badge-gray-bg: #374151;
      --badge-gray-border: #4b5563;
      --badge-gray-text: #f3f4f6;
      --badge-blue-bg: #1e3a8a;
      --badge-blue-border: #3b82f6;
      --badge-blue-text: #93c5fd;
    }
  }
  
  h1 {
    border-bottom: none !important;
    margin-bottom: 4px;
    margin-top: 0;
    letter-spacing: 0.5px;
    font-weight: 600;
  }
  
  .badge-text {
    letter-spacing: 1px;
    font-weight: 300;
  }
  
  .badge-container {
    display: inline-flex;
    align-items: center;
    background: var(--badge-gray-bg);
    border: 1px solid var(--badge-gray-border);
    border-radius: 6px;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 11px;
    text-decoration: none;
    vertical-align: middle;
  }

  .badge-container.blue {
    background: var(--badge-blue-bg);
    border-color: var(--badge-blue-border);
  }

  .badge-icon-section {
    padding: 4px 8px;
    border-right: 1px solid var(--badge-gray-border);
    display: flex;
    align-items: center;
  }

  .badge-text-section {
    padding: 4px 10px;
    color: var(--badge-gray-text);
    font-weight: 400;
  }

  .badge-container.blue .badge-text-section {
    color: var(--badge-blue-text);
  }
  
  .badge-link {
    text-decoration: none;
    margin-left: 8px;
    display: inline-flex;
    vertical-align: middle;
  }

  .badge-link:hover {
    text-decoration: none;
  }
  
  .badge-link:first-child {
    margin-left: 0;
  }
  
  .badge-icon-section svg {
    color: var(--badge-gray-text);
  }

  .badge-container.blue .badge-icon-section svg {
    color: var(--badge-blue-text);
  }
</style> 