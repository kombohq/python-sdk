# Assessment
(*assessment*)

## Overview

### Available Operations

* [get_packages](#get_packages) - Get packages
* [set_packages](#set_packages) - Set packages
* [get_open_orders](#get_open_orders) - Get open orders
* [update_order_result](#update_order_result) - Update order result

## get_packages

Get all available assessment and background check packages for an integration.

This is mainly intended for debugging. As you always need to submit the full list of available packages when using ["set packages"](/assessment/v1/put-packages), there shouldn't ever be a need to call this endpoint in production.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAssessmentPackages" method="get" path="/assessment/packages" -->
```python
from kombo import SDK


with SDK(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.assessment.get_packages()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.GetAssessmentPackagesRequest](../../models/getassessmentpackagesrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GetAssessmentPackagesPositiveResponse](../../models/getassessmentpackagespositiveresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.KomboAtsError   | default                | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## set_packages

Set packages

Replaces the list of available assessment and or background check packages.

Packages that have been previously submitted through this endpoint but aren't included again will be marked as deleted.

### Example Request Body

```json
{
  "packages": [
    {
      "id": "1001",
      "type": "SKILLS_TEST",
      "name": "TypeScript",
      "description": "TypeScript coding skills assessments"
    },
    {
      "id": "1002",
      "type": "VIDEO_INTERVIEW",
      "name": "Video Interview",
      "description": "Video interview to assess communication skills"
    }
  ]
}
```

### Example Usage

<!-- UsageSnippet language="python" operationID="PutAssessmentPackages" method="put" path="/assessment/packages" -->
```python
from kombo import SDK


with SDK(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.assessment.set_packages(packages=[
        {
            "id": "1001",
            "type": "SKILLS_TEST",
            "name": "TypeScript",
            "description": "TypeScript coding skills assessments",
        },
        {
            "id": "1002",
            "type": "VIDEO_INTERVIEW",
            "name": "Video Interview",
            "description": "Video interview to assess communication skills",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `packages`                                                                                                      | List[[models.PutAssessmentPackagesRequestBodyPackage](../../models/putassessmentpackagesrequestbodypackage.md)] | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.PutAssessmentPackagesPositiveResponse](../../models/putassessmentpackagespositiveresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.KomboAtsError   | default                | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_open_orders

Get all open assessment and background check orders of an integration.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAssessmentOrdersOpen" method="get" path="/assessment/orders/open" -->
```python
from kombo import SDK


with SDK(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.assessment.get_open_orders(page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                                     | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response. |
| `page_size`                                                                                                                  | *Optional[int]*                                                                                                              | :heavy_minus_sign:                                                                                                           | The number of results to return per page. Maximum is 250.                                                                    |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.GetAssessmentOrdersOpenResponse](../../models/getassessmentordersopenresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.KomboAtsError   | default                | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## update_order_result

Updates an assessment or a background check order result.

### Example Request Body

```json
{
  "status": "COMPLETED",
  "score": 90,
  "max_score": 100,
  "result_url": "https://example.com",
  "completed_at": "2023-04-04T00:00:00.000Z",
  "attributes": [
    {
      "type": "TEXT",
      "label": "Role fit",
      "value": "Excellent"
    },
    {
      "type": "SUB_RESULT",
      "id": "<YOUR_INTERNAL_ID_OF_THE_TEST>",
      "label": "Personality test",
      "score": {
        "value": 97,
        "max": 100
      },
      "status": "COMPLETED"
    }
  ],
  "attachments": [
    {
      "name": "Assessment Report.pdf",
      "data": "SGkgdGhlcmUsIEtvbWJvIGlzIGN1cnJlbnRseSBoaXJpbmcgZW5naW5lZXJzIHRoYXQgbG92ZSB0byB3b3JrIG9uIGRldmVsb3BlciBwcm9kdWN0cy4=",
      "content_type": "application/pdf"
    }
  ]
}
```

### Example Usage

<!-- UsageSnippet language="python" operationID="PutAssessmentOrdersAssessmentOrderIdResult" method="put" path="/assessment/orders/{assessment_order_id}/result" -->
```python
from kombo import SDK
from kombo.utils import parse_datetime


with SDK(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.assessment.update_order_result(assessment_order_id="GRKdd9dibYKKCrmGRSMJf3wu", status="COMPLETED", result_url="https://example.com", completed_at=parse_datetime("2023-04-04T00:00:00Z"), score=90, max_score=100, attributes=[
        {
            "type": "TEXT",
            "label": "Role fit",
            "value": "Excellent",
        },
        {
            "type": "SUB_RESULT",
            "id": "<YOUR_INTERNAL_ID_OF_THE_TEST>",
            "label": "Personality test",
            "score": {
                "value": 97,
                "max": 100,
            },
            "status": "COMPLETED",
        },
    ], attachments=[
        {
            "name": "Assessment Report.pdf",
            "content_type": "application/pdf",
            "data": "SGkgdGhlcmUsIEtvbWJvIGlzIGN1cnJlbnRseSBoaXJpbmcgZW5naW5lZXJzIHRoYXQgbG92ZSB0byB3b3JrIG9uIGRldmVsb3BlciBwcm9kdWN0cy4=",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assessment_order_id`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                        | PUT /assessment/orders/:assessment_order_id/result Parameter                                                                                                                                                                              |
| `status`                                                                                                                                                                                                                                  | [models.PutAssessmentOrdersAssessmentOrderIDResultRequestBodyStatus](../../models/putassessmentordersassessmentorderidresultrequestbodystatus.md)                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                        | Status of the assessment.<br/><br/>**Please note the `status` can only be updated to a different value if its current value is `OPEN`.**                                                                                                  |
| `result_url`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                       |
| `completed_at`                                                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                        | YYYY-MM-DDTHH:mm:ss.sssZ<br/><br/>**Please make sure this value is provided when the `status` is of the type `COMPLETED` or `CANCELLED`.**<br/><br/>[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString) |
| `score`                                                                                                                                                                                                                                   | *Optional[float]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                       |
| `max_score`                                                                                                                                                                                                                               | *Optional[float]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                       |
| `attributes`                                                                                                                                                                                                                              | List[[models.Attribute](../../models/attribute.md)]                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                        | An array of additional attributes that you would like to submit as a part of the assessment result.<br/><br/>- If an ATS only supports writing text attributes, we will transform non `TEXT` attributes into formatted plain text values. |
| `attachments`                                                                                                                                                                                                                             | List[[models.PutAssessmentOrdersAssessmentOrderIDResultRequestBodyAttachment](../../models/putassessmentordersassessmentorderidresultrequestbodyattachment.md)]                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                        | An array of attachments containing the assessment result.                                                                                                                                                                                 |
| `remote_fields`                                                                                                                                                                                                                           | [Optional[models.PutAssessmentOrdersAssessmentOrderIDResultRequestBodyRemoteFields]](../../models/putassessmentordersassessmentorderidresultrequestbodyremotefields.md)                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                        | Additional fields that we will pass through to specific ATS systems.                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                       |

### Response

**[models.PutAssessmentOrdersAssessmentOrderIDResultPositiveResponse](../../models/putassessmentordersassessmentorderidresultpositiveresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.KomboAtsError   | default                | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |