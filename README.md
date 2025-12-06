# Kombo Python SDK

Developer-friendly & type-safe Python SDK for the [Kombo Unified API](https://docs.kombo.dev/introduction).

<div align="left">
  <a href="https://www.speakeasy.com/?utm_source=kombo-python&utm_campaign=python">
    <img src="https://custom-icon-badges.demolab.com/badge/-built%20with%20speakeasy-212015?style=flat-square&logoColor=FBE331&logo=speakeasy&labelColor=545454" />
  </a>
  <a href="https://pypi.org/project/kombo/">
    <img src="https://img.shields.io/pypi/v/kombo?style=flat-square" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" />
  </a>
</div>

<br />

> [!NOTE]
> The Kombo Python SDK is **currently in beta**. The core API structure, methods, and input/output objects are considered stable. We may still make minor adjustments such as renames to exported type classes or fixes for code generator oddities, but all changes will be clearly documented in the changelog. We **do not foresee** any blockers for production use.

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Kombo Python SDK](#kombo-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Region Selection](#region-selection)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [Error Handling](#error-handling)
  * [Retries](#retries)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Contributions](#contributions)

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
uv add kombo
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install kombo
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add kombo
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from kombo python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "kombo",
# ]
# ///

from kombo import Kombo

sdk = Kombo(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

## SDK Example Usage

```python
from kombo import SDK


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)
```

### Specifying an integration ID

The majority of Kombo API endpoints are for interacting with a single "integration" (i.e., a single connection to one your customers' systems). For using these, make sure to specify the `integration_id` parameter when initializing the SDK:

```python
from kombo import SDK


with SDK(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
) as sdk:

    res = sdk.hris.get_employees()

    # Handle response
    print(res)
```

## Region Selection

The Kombo platform is available in two regions: Europe and United States.

By default, the SDK will use the EU region. If you're using the US region (hosted under `api.us.kombo.dev`), make sure to specify the `server` parameter when initializing the SDK.

#### Example

```python
from kombo import SDK


with SDK(
    server="us",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.general.check_api_key()

    # Handle response
    print(res)

```

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Assessment](docs/sdks/assessment/README.md)

* [get_packages](docs/sdks/assessment/README.md#get_packages) - Get packages
* [set_packages](docs/sdks/assessment/README.md#set_packages) - Set packages
* [get_open_orders](docs/sdks/assessment/README.md#get_open_orders) - Get open orders
* [update_order_result](docs/sdks/assessment/README.md#update_order_result) - Update order result

### [Ats](docs/sdks/ats/README.md)

* [get_applications](docs/sdks/ats/README.md#get_applications) - Get applications
* [move_application_to_stage](docs/sdks/ats/README.md#move_application_to_stage) - Move application to stage
* [add_application_result_link](docs/sdks/ats/README.md#add_application_result_link) - Add result link to application
* [add_application_note](docs/sdks/ats/README.md#add_application_note) - Add note to application
* [get_application_attachments](docs/sdks/ats/README.md#get_application_attachments) - Get application attachments
* [add_application_attachment](docs/sdks/ats/README.md#add_application_attachment) - Add attachment to application
* [reject_application](docs/sdks/ats/README.md#reject_application) - Reject application
* [get_candidates](docs/sdks/ats/README.md#get_candidates) - Get candidates
* [create_candidate](docs/sdks/ats/README.md#create_candidate) - Create candidate
* [get_candidate_attachments](docs/sdks/ats/README.md#get_candidate_attachments) - Get candidate attachments
* [add_candidate_attachment](docs/sdks/ats/README.md#add_candidate_attachment) - Add attachment to candidate
* [add_candidate_result_link](docs/sdks/ats/README.md#add_candidate_result_link) - Add result link to candidate
* [add_candidate_tag](docs/sdks/ats/README.md#add_candidate_tag) - Add tag to candidate
* [remove_candidate_tag](docs/sdks/ats/README.md#remove_candidate_tag) - Remove tag from candidate
* [get_tags](docs/sdks/ats/README.md#get_tags) - Get tags
* [get_application_stages](docs/sdks/ats/README.md#get_application_stages) - Get application stages
* [get_jobs](docs/sdks/ats/README.md#get_jobs) - Get jobs
* [create_application](docs/sdks/ats/README.md#create_application) - Create application
* [get_users](docs/sdks/ats/README.md#get_users) - Get users
* [get_offers](docs/sdks/ats/README.md#get_offers) - Get offers
* [get_rejection_reasons](docs/sdks/ats/README.md#get_rejection_reasons) - Get rejection reasons
* [get_interviews](docs/sdks/ats/README.md#get_interviews) - Get interviews
* [import_tracked_application](docs/sdks/ats/README.md#import_tracked_application) - Import tracked application

### [Connect](docs/sdks/connect/README.md)

* [create_connection_link](docs/sdks/connect/README.md#create_connection_link) - Create connection link
* [get_integration_by_token](docs/sdks/connect/README.md#get_integration_by_token) - Get integration by token

### [General](docs/sdks/general/README.md)

* [check_api_key](docs/sdks/general/README.md#check_api_key) - Check API key
* [trigger_sync](docs/sdks/general/README.md#trigger_sync) - Trigger sync
* [send_passthrough_request](docs/sdks/general/README.md#send_passthrough_request) - Send passthrough request
* [delete_integration](docs/sdks/general/README.md#delete_integration) - Delete integration
* [get_integration_details](docs/sdks/general/README.md#get_integration_details) - Get integration details
* [create_reconnection_link](docs/sdks/general/README.md#create_reconnection_link) - Create reconnection link
* [get_integration_fields](docs/sdks/general/README.md#get_integration_fields) - Get integration fields
* [update_integration_field](docs/sdks/general/README.md#update_integration_field) - Updates an integration fields passthrough setting
* [get_custom_fields](docs/sdks/general/README.md#get_custom_fields) - Get custom fields with current mappings
* [update_custom_field_mapping](docs/sdks/general/README.md#update_custom_field_mapping) - Put custom field mappings
* [get_tools](docs/sdks/general/README.md#get_tools) - Get tools

### [Hris](docs/sdks/hris/README.md)

* [get_employees](docs/sdks/hris/README.md#get_employees) - Get employees
* [get_employee_form](docs/sdks/hris/README.md#get_employee_form) - Get employee form
* [create_employee_with_form](docs/sdks/hris/README.md#create_employee_with_form) - Create employee with form
* [add_employee_document](docs/sdks/hris/README.md#add_employee_document) - Add document to employee
* [get_employee_document_categories](docs/sdks/hris/README.md#get_employee_document_categories) - Get employee document categories
* [get_groups](docs/sdks/hris/README.md#get_groups) - Get groups
* [get_employments](docs/sdks/hris/README.md#get_employments) - Get employments
* [get_locations](docs/sdks/hris/README.md#get_locations) - Get work locations
* [get_absence_types](docs/sdks/hris/README.md#get_absence_types) - Get absence types
* [get_time_off_balances](docs/sdks/hris/README.md#get_time_off_balances) - Get time off balances
* [get_absences](docs/sdks/hris/README.md#get_absences) - Get absences
* [create_absence](docs/sdks/hris/README.md#create_absence) - Create absence
* [delete_absence](docs/sdks/hris/README.md#delete_absence) - Delete absence
* [get_legal_entities](docs/sdks/hris/README.md#get_legal_entities) - Get legal entities
* [get_timesheets](docs/sdks/hris/README.md#get_timesheets) - Get timesheets
* [get_performance_review_cycles](docs/sdks/hris/README.md#get_performance_review_cycles) - Get performance review cycles
* [get_performance_reviews](docs/sdks/hris/README.md#get_performance_reviews) - Get performance reviews

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.get_integration_fields(integration_id="<id>", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKError`](./src/kombo/errors/sdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from kombo import Kombo, errors


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:
    res = None
    try:

        res = k_client.general.check_api_key()

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
* [`SDKError`](./src/kombo/errors/sdkerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (8)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKError`](./src/kombo/errors/sdkerror.py)**:
* [`KomboAtsError`](./src/kombo/errors/komboatserror.py): The standard error response with the error codes for the ATS use case. Applicable to 27 of 57 methods.*
* [`KomboHrisError`](./src/kombo/errors/kombohriserror.py): The standard error response with the error codes for the HRIS use case. Applicable to 17 of 57 methods.*
* [`KomboGeneralError`](./src/kombo/errors/kombogeneralerror.py): The standard error response with just the platform error codes. Applicable to 13 of 57 methods.*
* [`ResponseValidationError`](./src/kombo/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from kombo import Kombo
from kombo.utils import BackoffStrategy, RetryConfig


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.check_api_key(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from kombo import Kombo
from kombo.utils import BackoffStrategy, RetryConfig


with Kombo(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.check_api_key()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from kombo import Kombo
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Kombo(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from kombo import Kombo
from kombo.httpclient import AsyncHttpClient
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

s = Kombo(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Kombo` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from kombo import Kombo
def main():

    with Kombo(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as k_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Kombo(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ) as k_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from kombo import Kombo
import logging

logging.basicConfig(level=logging.DEBUG)
s = Kombo(debug_logger=logging.getLogger("kombo"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=kombo-python&utm_campaign=python)

<!-- No Summary [summary] -->
<!-- No SDK Example Usage [usage] -->
<!-- No IDE Support [idesupport] -->
<!-- No Authentication [security] -->
<!-- No Global Parameters [global-parameters] -->
<!-- No Server Selection [server] -->
