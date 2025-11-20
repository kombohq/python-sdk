# General
(*general*)

## Overview

### Available Operations

* [check_api_key](#check_api_key) - Check API key
* [trigger_sync](#trigger_sync) - Trigger sync
* [send_passthrough_request](#send_passthrough_request) - Send passthrough request
* [delete_integration](#delete_integration) - Delete integration
* [get_integration_details](#get_integration_details) - Get integration details
* [create_reconnection_link](#create_reconnection_link) - Create reconnection link
* [get_integration_fields](#get_integration_fields) - Get integration fields
* [update_integration_field](#update_integration_field) - Updates an integration fields passthrough setting
* [get_custom_fields](#get_custom_fields) - Get custom fields with current mappings
* [update_custom_field_mapping](#update_custom_field_mapping) - Put custom field mappings
* [get_tools](#get_tools) - Get tools

## check_api_key

Check whether your API key is working properly.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCheckApiKey" method="get" path="/check-api-key" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.check_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCheckAPIKeyPositiveResponse](../../models/getcheckapikeypositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## trigger_sync

Trigger a sync for a specific integration.

<Warning>Please note that it is **not** necessary nor recommended to call this endpoint periodically on your side. Kombo already performs periodic syncs for you and you should only trigger syncs yourself in special cases (like when a user clicks on a "Sync" button in your app).</Warning>

### Example Usage

<!-- UsageSnippet language="python" operationID="PostForceSync" method="post" path="/force-sync" -->
```python
from kombo import Kombo


with Kombo(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.trigger_sync(type_="FULL")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `type`                                                                                        | [Optional[models.PostForceSyncRequestBodyType]](../../models/postforcesyncrequestbodytype.md) | :heavy_minus_sign:                                                                            | The type of the triggered sync.                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.PostForceSyncPositiveResponse](../../models/postforcesyncpositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## send_passthrough_request

Send a request to the specified integration's native API.

At Kombo we put a lot of work into making sure that our unified API covers all our customers' use cases and that they never have to think about integration-specific logic again. There are cases, however, where our customers want to build features that are very integration-specific. That's where this endpoint comes in.

Pass in details about the request you want to make to the integration's API and we'll forward it for you. We'll also take care of setting the right base URL and authenticating your requests.

To get started, please pick the relevant API (some tools provide multiple to due different base URLs or authentication schemes) from the table below and pass in the `{tool}/{api}` identifier as part of the path.

|Integration|`{tool}/{api}`|Description|
|---|---|---|
|Personio|`personio/personnel`|Personio's [Personnel Data API](https://developer.personio.de/reference/get_company-employees). We automatically authenticate all requests using the client ID and secret and use `https://api.personio.de/v1` as the base URL.|
|Personio|`personio/personnelv2`|Personio's [V2 Personnel Data API](https://developer.personio.de/v2.0/reference/introduction). We automatically authenticate all requests using the client ID and secret and use `https://api.personio.de/v2` as the base URL.|
|Workday|`workday/soap`|[Workday's SOAP API](https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html). We automatically authenticate all requests. Set `data` to your raw xml string. Use `/` as your `path`, as we will always send requests to `https://\{domain\}/ccx/service/\{tenant\}/\{service_name\}`. Set your `method` to `POST`. You need to specify the `api_options` object and set `service_name` to the name of the service you want to call. Find all available services [here](https://community.workday.com/sites/default/files/file-hosting/productionapi/versions/v41.0/index.html). The string that you submit as `data` will be the content of the `soapenv:Body` tag in the request. You can set the `service_version` to any valid Workday service version (the default is `38.2`).|
|Workday|`workday/rest`|[Workday's REST API](https://community.workday.com/sites/default/files/file-hosting/restapi/index.html). We automatically authenticate all requests and use the correct Workday REST base URL for your tenant. The base URL follows the format: https://\{domain\}/api/\{service_name\}/\{version\}/\{tenant\}. You can specify any valid REST endpoint and method. See the Workday REST API documentation for available endpoints. You must specify the `api_options` object and set `service_name` to the name of the service you want to call. You can also specify the `version` (e.g., "v1", "v2"); if omitted, it defaults to "v1".|
|SAP SuccessFactors|`successfactors/odata-v2`|[SuccessFactors' OData V2 API](https://help.sap.com/doc/74597e67f54d4f448252bad4c2b601c9/2211/en-US/SF_HCM_OData_API_REF_en.pdf). We automatically authenticate all requests and use `https://\{api_domain\}\{path?\}/odata/v2` as the base URL (the optional `\{path\}` is used when connecting via proxied/gateway domains).|
|SmartRecruiters|`smartrecruiters/default`|Smartrecruiters [API](https://developers.smartrecruiters.com/reference/apply-api). We automatically authenticate all requests using OAuth and use `https://api.smartrecruiters.com` as the base URL.|
|SmartRecruiters|`smartrecruiters/default`|Smartrecruiters [API](https://developers.smartrecruiters.com/reference/apply-api). We automatically authenticate all requests using the credentials supplied by the customer and use `https://api.smartrecruiters.com` as the base URL.|
|Factorial|`factorial/api`|Factorial's [API](https://apidoc.factorialhr.com/). We automatically authenticate all requests and use `https://api.factorialhr.com/api` or `https://api.demo.factorial.dev/api` as the base URL, depending on the connected instance.|
|Oracle Recruiting Cloud|`oraclerecruiting/rest`|[Oracles's REST API](https://docs.oracle.com/en/cloud/saas/human-resources/24d/farws/rest-endpoints.html). We automatically authenticate all requests and use 'https://\{company_url\}' as the base url.|
|Oracle Recruiting Cloud|`oraclerecruiting/rest`|[Oracle's REST API](https://docs.oracle.com/en/cloud/saas/human-resources/24d/farws/rest-endpoints.html). We automatically authenticate all requests and use 'https://\{company_url\}' as the base url.|
|Lever|`lever/v1`|[Lever's v1 API](https://hire.lever.co/developer/documentation). We automatically authenticate all requests using the partner credentials which have been configured in the Lever tool settings (this uses Kombo's partner credentials by default).|
|iCIMS|`icims/default`|[iCIMS Default API](https://developer-community.icims.com/). We automatically authenticate all requests and use `https://api.icims.com/customers/\{customer_id\}` as the base url.|
|Recruitee|`recruitee/default`|The [Recruitee API](https://api.recruitee.com/docs/index.html). We automatically authenticate all requests and use `https://api.recruitee.com/c/\{company_id\}` as the base URL.|
|RecruiterFlow|`recruiterflow/v1`|RecruiterFlow API [docs](https://docs.recruiterflow.com/). We automatically authenticate all requests using the RF-Api-Key header and use `https://api.recruiterflow.com` as the base URL.|
|Greenhouse|`greenhouse/harvest`|Greenhouse [Harvest API](https://developers.greenhouse.io/harvest.html). We automatically authenticate all requests using the API key and use `https://harvest.greenhouse.io/v1` as the base URL.|
|Greenhouse Job Board|`greenhousejobboard/boards-api`|[Greenhouse Job Board API](https://developers.greenhouse.io/job-board). We automatically authenticate all requests and use 'https://boards-api.greenhouse.io/v1/boards/\{job_board_token\}' as the base URL. Optionally, you can provide a custom job_board_token to use a different job board.|
|Teamtailor|`teamtailor/v1`|Teamtailor's [JSON-API](https://docs.teamtailor.com/). We authenticate all request with the Teamtailor API key and use the base URL `https://api.teamtailor.com/v1`.|
|Teamtailor Job Boards|`teamtailorjobboards/direct-apply`|Teamtailor's [Job Board Direct Apply API](https://partner.teamtailor.com/job_boards/direct_apply/#direct-apply). We automatically authenticate all requests and use `https://5qbn6o9x4h.execute-api.eu-west-1.amazonaws.com/production` as the base URL. All requests are automatically signed with HMAC-SHA256 signature.|
|Ashby|`ashby/v1`|Ashby's [V1 API](https://developers.ashbyhq.com/reference/introduction). We automatically authenticate all requests with the provided credentials and use `https://api.ashbyhq.com` as the base URL. Please note that Ashby uses an RPC-style API. Please check [the Ashby API documentation](https://developers.ashbyhq.com/reference/introduction) for details on how to use it.|
|CEGID TalentSoft FrontOffice|`talentsoft/v2`|Cegid Talentsoft Recruiting FrontOffice [API](https://developers.cegid.com/api-details). We automatically authenticate all requests using the provided credentials and use `https://\{domain\}/api/v2` as the base URL.|
|CEGID TalentSoft Customer|`talentsoftcustomer/v1`|Cegid Talentsoft Recruiting FrontOffice API: [API Documentation](https://developers.cegid.com/api-details#api=cegid-talentsoft-recruiting-frontoffice) We automatically authenticate all requests and use `https://\{customer_subdomain\}.talent-soft.com/api/v1` as the base URL.|
|Talention|`talention/v1`|Talention's API. We automatically authenticate all requests and use `https://\{api_domain\}/tms/\{account_id\}/external/api/1.0` as the base URL. Documentation is provided privately by Talention. Contact Kombo support for assistance with specific endpoints.|
|Onlyfy|`onlyfy/v1`|Onlyfy's [Public v1 REST API](https://onlyfy.io/doc/v1#section/Introduction). We automatically authenticate all requests using the `apikey` header and use `https://api.prescreenapp.io/v1` as the base URL.|
|Personio|`personio/recruiting`|Personio's [Recruiting API](https://developer.personio.de/reference/get_company-employees). We automatically authenticate all requests using the Recruiting access token and use `https://api.personio.de/v1/recruiting` as the base URL.|
|Personio|`personio/recruitingV2`|Personio's [V2 Recruiting API](https://developer.personio.de/reference/get_v2-recruiting-applications). We automatically authenticate all requests using the Recruiting access token, send the `Beta` header and use `https://api.personio.de/v2/recruiting` as the base URL.|
|Personio|`personio/jobboard`|API endpoints exposed on Personio's public job board pages ([currently just the XML feed](https://developer.personio.de/reference/get_xml)). We automatically use the right `https://\{company\}.jobs.personio.de` base URL.|
|UKG Pro|`ukgpro/recruting`|[UKG Pro's Recruiting API](https://developer.ukg.com/hcm/reference/retrieveapplications). We automatically authenticate all requests and use  `https://\{hostname\}/talent/recruiting/v2/\{tenantalias\}/api` as the base URL.|
|UKG Pro|`ukgpro/default`|[UKG Pro's HRIS API](https://developer.ukg.com/hcm/reference/get_personnel-v1-person-details). We automatically authenticate all requests and use  `https://\{hostname\}` as the base URL.|
|UKG Ready|`ukgready/api`|UKG Ready [API](https://secure.saashr.com/ta/docs/rest/public/). We automatically authenticate all requests using the provided credentials and use `https://\{api_domain\}` as the base URL.|
|UKG Ready|`ukgready/api`|UKG Ready [API](https://secure.saashr.com/ta/docs/rest/public/). We automatically authenticate all requests using the provided credentials and use `https://\{api_domain\}` as the base URL.|
|ADP Workforce Now|`adpworkforcenow/default`|[ADP Workforce Now API v2](https://developers.adp.com/build/api-explorer/hcm-offrg-wfn). We automatically authenticate all requests and use the correct subdomain.|
|Taleo|`taleo/soap`|[Taleo's API](https://docs.oracle.com/en/cloud/saas/taleo-enterprise/23b/otwsu/c-taleoapi.html). We automatically authenticate all requests and use 'https://\{your-subdomain\}.taleo.net/enterprise/soap' as base URL.|
|rexx systems|`rexx/default`|Rexx's HRIS export API. There is only one endpoint: `Get /`|
|AFAS Software|`afas/api`|AFAS' [API](https://connect.afas.nl/rest/get). We automatically authenticate all requests and use `https://\{domain\}/ProfitRestServices` as the base URL.|
|BambooHR|`bamboohr/v1`|BambooHR's [API](https://documentation.bamboohr.com/reference/get-employee). We automatically authenticate all requests using the customer credentials `https://api.bamboohr.com/api/gateway.php/\{subdomain\}/v1` as the base URL.|
|Bullhorn|`bullhorn/default`|[Bullhorn's API](https://bullhorn.github.io/rest-api-docs/index.html). We automatically use the right `https://rest.bullhornstaffing.com/rest-services/\{corpToken\}` base URL.|
|Workable|`workable/v1`|Workable's [API](https://workable.readme.io/reference/generate-an-access-token). We automatically authenticate all requests using the client ID and secret and use `https://\{subdomain\}.\{environment\}.com/spi/v3` as the base URL.|
|PayFit|`payfitcustomer/api`|PayFit [Partner API](https://developers.payfit.io/reference). We automatically authenticate all requests using the provided API key and use `https://partner-api.payfit.com` as the base URL.|
|PayFit|`payfitpartner/partner-api`|PayFit [Partner API](https://developers.payfit.io/reference). We automatically authenticate all requests using the OAuth access token and use `https://partner-api.payfit.com` as the base URL.|
|Jobvite|`jobvite/api`|We automatically authenticate all requests and use 'https://api.jobvite.com/api/v2' as the base URL.|
|Employment Hero|`employmenthero/default`|EmploymentHero [API](https://developer.employmenthero.com/api-references/#icon-book-open-introduction). We automatically authenticate all requests using the credentials supplied by the customer and use `https://api.employmenthero.com/api` as the base URL.|
|Fountain|`fountain/v2`|Fountain's [Hire API](https://developer.fountain.com/reference/get_v2-applicants). We automatically authenticate all requests and use `https://api.fountain.com/v2` as the base URL.|
|Fourth|`fourth/uk-employee`|Fourth [UK Employee API](https://developer.fourth.com/en-gb/docs/uk-employee-api/reference) We automatically authenticate all requests and use `https://api.fourth.com/hr/organisations/\{organisation_id\}/` as the base URL. We also enforce the required query params for all requests.|
|Kenjo|`kenjo/api`|Kenjo's [API](https://kenjo.readme.io/reference/generate-the-api-key). We automatically authenticate all requests using the API key and use `https://api.kenjo.io/` as the base URL.|
|HeavenHR|`heavenhr/v2`|[HeavenHR API](https://api.heavenhr.com/). We automatically authenticate all requests using the provided credentials and use `https://api.heavenhr.com/api/v2` as the base URL.|
|HiBob|`hibob/v1`|[HibBob's v1 API](https://apidocs.hibob.com/reference/get_people). We automatically authenticate all requests using the service user credentials (or, for old integrations, the API key) and use `https://api.hibob.com/v1` as the base URL.|
|HiBob|`hibob/hire`|[HiBob's Hire API](https://apidocs.hibob.com/docs/how-to-integrate-with-ats-hire-api). We automatically authenticate all requests using the hire service user credentials. The base URL is configured during the integration setup.|
|Softgarden|`softgarden/frontend-v3`|[Softgarden's Frontend API v3](https://dev.softgarden.de/frontend-v3/. We automatically authenticate all requests and use 'https://api.softgarden.io/api/rest' as base URL.|
|Softgarden|`softgarden/apply-api`|[Softgarden's Apply API](https://dev.softgarden.de/apply-api/). We automatically authenticate all requests and use 'https://jobdb.softgarden.de/jobdb/public' as base URL.|
|Cezanne HR|`cezannehr/dataservice`|[CezanneHR's v7 dataservice API](https://api.cezannehr.com/).We automatically authenticate all requests and use the base URL `https://subdomain.cezanneondemand.com/cezanneondemand/v7/dataservice.svc`|
|Microsoft Entra ID|`entraid/v1`|[AzureAD's API](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0). We automatically authenticate all requests.|
|Microsoft Azure AD|`azuread/v1`|[AzureAD's API](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0). We automatically authenticate all requests.|
|Google Workspace|`googleworkspace/people`|[Googles's API](https://developers.google.com/people/api/rest). We automatically authenticate all requests and use 'https://people.googleapis.com' as the base URL.|
|Google Workspace|`googleworkspace/admin`|[Googles's API](https://developers.google.com/admin-sdk/directory/reference/rest). We automatically authenticate all requests and use 'https://admin.googleapis.com' as the base URL.|
|Nmbrs|`nmbrs/soap`|[Nmbrs SOAP API](https://api.nmbrs.nl/soap/v3/). We automatically authenticate all requests and use `https://api.nmbrs.nl/soap/v3/` as the base URL. Set `data` to your raw XML string (the content that will be placed inside the `\<soap:Body\>` tag). Use `/` as your `path`, as we will always send requests to `https://api.nmbrs.nl/soap/v3/\{service_name\}.asmx`. Set your `method` to `POST`. You need to specify the `api_options` object and set `service_name` to the name of the service you want to call. Available services include `EmployeeService` and `CompanyService`.|
|Pinpoint|`pinpoint/v1`|Pinpoint's [JSON:API](https://developers.pinpointhq.com/docs). We automatically authenticate all requests using the `X-API-KEY` header and use `https://\{subdomain\}.pinpointhq.com/api/v1` as the base URL.|
|d.vinci|`dvinci/rest-api`|The [DVinci REST API](https://static.dvinci-easy.com/files/d.vinci%20rest-api.html). All requests are authenticated by Kombo and use `https://\{dvinci_domain\}/restApi/` as the base URL.|
|d.vinci|`dvinci/apply-api`|The [DVinci Apply API](https://static.dvinci-easy.com/files/d.vinci%20application-apply-api.html). All requests are authenticated by Kombo and use `https://\{dvinci_domain\}/p/\{portal_path\}/` as the base URL.|
|d.vinci admin|`dvinciadmin/rest-api`|[DVinci REST API](https://static.dvinci-easy.com/files/d.vinci%20rest-api.html).|
|d.vinci admin|`dvinciadmin/odata-api`|[DVinci ODATA API](https://dvinci.freshdesk.com/en/support/solutions/articles/75000059523-odata-reporting-api).|
|JOIN|`join/v2`|Join's [V2 API](https://docs.join.com/reference/getting-started). We automatically authenticate all requests and use `https://api.join.com/v2` as the base URL.|
|Deel|`deel/api`|Deel's [API](https://developer.deel.com/reference/). We automatically authenticate all requests using the provided credentials and use `https://\{api_domain\}/rest` as the base URL.|
|Remote|`remotecom/default`|Remote's [API](https://remote.com/resources/api/getting-started). We automatically authenticate all requests using provided credentials.|
|IRIS Cascade|`iriscascade/v2`|IRIS Cascade HR [API](https://swagger.hrapi.co.uk/). We automatically authenticate all requests using the provided credentials and use `https://api.iris.co.uk/hr/v2` as the base URL.|
|Okta|`okta/v1`|[Okta's API](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/ApiServiceIntegrations/). We automatically authenticate all request ans use 'https://\<your-okta-domain\>/api/v1' as the base URL.|
|Sage HR|`sagehr/api`|Sage HR's [API](https://developer.sage.com/hr/reference/api-ref). We automatically authenticate all requests and use `https://\{subdomain\}.sage.hr/api` as the base URL.|
|Sage People|`sagepeople/salesforce-rest-api`|Sage People is built on Salesforce's [API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm). We automatically authenticate all requests and use `https://\{customer_name\}.my.salesforce.com/` as the base URL.|
|Humaans|`humaans/api`|Humaans' [API](https://docs.humaans.io/api/). We automatically authenticate all requests using the API key and use `https://app.humaans.io/api` as the base URL.|
|TRAFFIT|`traffit/v2`|Traffit's [v2 API](https://api.traffit.com). We authenticate all requests with the Traffit API key and use the base URL `https://yourdomain.traffit.com/api/integration/v2`.|
|eRecruiter|`erecruiter/api`|[eRecruiter's API](https://api.erecruiter.net/swagger/ui/index). We automatically authenticate all requests and use `https://\{domain\}/Api` as the base URL.|
|Eurécia|`eurecia/api`|Eurécia [REST API](https://api.eurecia.com/eurecia/fw/swagger/index.html#/) We automatically authenticate all requests and use `https://\{domain\}/eurecia/rest` as the base URL.|
|Abacus Umantis|`abacusumantis/v1`|[Umantis API v1](https://recruitingapp-91005709.umantis.com/api/v1/swagger-ui). We automatically authenticate all requests and use `https://\{subdomain\}.umantis.com/api/v1` as the base URL.|
|Haufe Umantis|`umantis/v1`|[Umantis API v1](https://recruitingapp-91005709.umantis.com/api/v1/swagger-ui). We automatically authenticate all requests and use `https://\{subdomain\}.umantis.com/api/v1` as the base URL.|
|Jobylon|`jobylon/push`|The [Jobylon Push API](https://developer.jobylon.com/push-api-and-webhooks/). We automatically authenticate all requests and use `https://\{subdomain\}.jobylon.com/p1` as the base URL.|
|Jobylon|`jobylon/feed`|The [Jobylon Feed API](https://developer.jobylon.com/feed-api/). We automatically authenticate all requests and use `https://\{subdomain\}.jobylon.com/feeds/\{job_hash\}` as the base URL.|
|Oracle HCM|`oraclehcm/api`|Oracle HCM Cloud [REST API](https://docs.oracle.com/en/cloud/saas/human-resources/24d/farws/index.html). We automatically authenticate all requests and use `https://\{domain\}/` as the base URL, where domain is your Oracle Cloud domain.|
|Taleez|`taleez/0`|[Taleez's API](https://api.taleez.com/swagger-ui/index.html). We automatically authenticate all requests and use `https://api.taleez.com/0` as the base URL.|
|HR WORKS|`hrworks/v2`|HRWorks's v2 [API](https://developers.hrworks.de/2.0/endpoints). We automatically authenticate all requests using the customer credentials.|
|Abacus|`abacus/api`|Abacus [REST API](https://apihub.abacus.ch/). We automatically authenticate all requests and use `https://\{\{abacusUrl\}\}/api/entity/v1/mandants/\{\{mandantId\}\}` as the base URL.|
|Zoho Recruit|`zohorecruit/v2`|Zoho Recruit's [V2 API](https://www.zoho.com/recruit/developer-guide/apiv2/modules-api.html). We automatically authenticate all requests and use `https://recruit.\{domain\}/recruit/v2` as the base URL.|
|AlexisHR|`alexishr/v1`|[AlexisHR's v1 API](https://docs.alexishr.com/) We automatically authenticate all requests and use `https://\{subdomain\}.alexishr.com` as base URL.|
|Simployer|`simployer/v1`|[AlexisHR's v1 API](https://docs.alexishr.com/) We automatically authenticate all requests and use `https://\{subdomain\}.alexishr.com` as base URL.|
|Eploy|`eploy/api`|Eploy's [API](https://www.eploy.com/resources/developers/api-documentation/). We automatically authenticate all requests and use `https://\{subdomain\}.eploy.net/api` as the base URL.|
|JobDiva|`jobdiva/api`|We automatically authenticate all requests and use `https://api.jobdiva.com` as the base URL.|
|Visma Peple|`peple/hrm`|[Visma Payroll Reporting API](https://api.analytics1.hrm.visma.net/docs/openapi.html). We automatically authenticate all requests using the client credentials and use 'https://api.analytics1.hrm.visma.net' as the base URL.|
|Visma YouServe|`youserve/learning`|Visma YouServe [Learning API](https://youserve-domain-api.github.io/SwaggerUI/learning.html). We automatically authenticate all requests using OAuth 2.0 with the provided credentials and use `https://api.youserve.nl/learning/v1.0` as the base URL.|
|Dayforce|`dayforce/V1`|[Dayforce's API](https://developers.dayforce.com/Build/Home.aspx). We automatically authenticate all requests and use `\{\{baseUrl\}\}/Api/\{\{clientNamespace\}\}/V1` as the base URL|
|Hansalog|`hansalog/vision`|Hansalog's [Vision API](https://hansalog-vision.document360.io/docs/). We automatically authenticate all requests and use `https://\{subdomain\}.hansalog-cloud.de/vision` as the base URL.|
|Lattice|`lattice/passthrough`|Lattice's [API](https://developers.lattice.com/v2/docs/base-url-1). We automatically authenticate all requests using OAuth credentials with `https://api.latticehq.com` as the base URL.|
|Lattice|`lattice/talent`|Lattice's [Talent API](https://developers.lattice.com/docs/introduction-1). We automatically authenticate all requests using OAuth credentials with `https://api.latticehq.com` as the base URL.|
|Paylocity|`paylocity/default`|[Paylocity's Weblink API](https://developer.paylocity.com/integrations/reference/authentication-weblink). We automatically authenticate all requests and use 'https://\{api|dc1demogw\}.paylocity.com/' as the base URL.|
|Paylocity|`paylocity/next-gen`|[Paylocity's NextGen API](https://developer.paylocity.com/integrations/reference/authentication). We automatically authenticate all requests and use 'https://dc1prodgwext.paylocity.com/' as the base URL.|
|Paycor|`paycor/v1`|[Paycors's v1 API](https://developers.paycor.com/explore#section/Getting-Started). We automatically authenticate all requests and use 'https://apis.paycor.com'.|
|Paycom|`paycom/v1`|Paycom's REST API. We automatically authenticate all requests using the provided SID and API Token and use `https://api.paycomonline.net/v4/rest/index.php/api/v1` as the base URL.|
|Insperity|`insperity/api`|Insperity [APIs](https://developer.insperity.com/) We automatically authenticate all requests and use `https://api.insperity.com` as the base URL. For staging environments, we use `https://apistage.insperity.com`. Note that all requests require the company ID to be specified in the path or body.|
|Paychex|`paychex/api`|Paychex [REST API](https://developer.paychex.com/documentation). We automatically authenticate all requests and use `https://api.paychex.com` as the base URL.|
|Avature|`avature/custom-api`|Avatures's Custom API. Call `Get /openapi` to retrieve the specific custom API schema. We automatically authenticate all requests and use the instance specific custom API URL as the base URL.|
|Apploi|`apploi/rest-api`|The [Apploi API](https://integrate.apploi.com/). We automatically authenticate all requests and use `https://partners.apploi.com/` as the base URL.|
|Phenom|`phenom/rest-api`|The [Phenom API](https://developer.phenom.com/). We automatically authenticate all requests and use `https://api-stg.phenompro.com` as the base URL.|
|Rippling|`rippling/api`|Rippling's [API](https://developer.rippling.com/documentation). We automatically authenticate all requests and use `https://api.rippling.com/platform/api` or`https://rest.ripplingapis.com` as the base URL.|
|Heyrecruit|`heyrecruit/v2`|[Heyrecruit's v2 API](https://documenter.getpostman.com/view/23241256/2s9YysBLcf#47e271ac-47c8-4c75-9cc6-b8c506e9dad6). We automatically authenticate all requests using the client ID and secret and use `https://app.heyrecruit.de/api/v2` as the base URL.|
|PeopleHR|`peoplehr/default`|[PeopleHR's API](https://apidocs.peoplehr.com/#). We automatically authenticate all request ans use 'https://api.peoplehr.net' as the base URL.|
|JazzHR|`jazzhr/v1`|[JazzHR's v1 API](https://www.resumatorapi.com/v1/#!`).We automatically authenticate all requests and use "https://api.resumatorapi.com/v1/" as the base URL.|
|Lucca|`lucca/api`|[Luccas's API](https://developers.lucca.fr/api-reference/legacy/introduction). We automatically authenticate all requests and use 'https://\{account\}.\{ilucca|ilucca-demo\}.\{region\}/' as the base URL.|
|BITE|`bite/v1`|[Bite's v1 API](https://api.b-ite.io/docs/#/). We automatically authenticate all requests and use 'https://api.b-ite.io/v1' as base URL.|
|Zelt|`zelt/partner`|Zelt's [Partner API](https://go.zelt.app/apiv2/swagger). We automatically authenticate all requests using the connected OAuth credentials and use `https://go.zelt.app/apiv2/partner` as the base URL.|
|Planday|`planday/api`|Planday's [HR API v1.0](https://openapi.planday.com/api/hr?version=v1.0). We automatically authenticate all requests and use `https://openapi.planday.com` as the base URL.|
|Hailey HR|`haileyhr/api`|Hailey HR's [API](https://api.haileyhr.app/docs/index.html). We automatically authenticate all requests using the provided credentials and use `https://api.haileyhr.app` as the base URL.|
|Silae|`silae/rest`|[Silae's REST API](https://silae-api.document360.io/docs). We automatically authenticate all requests and use 'https://payroll-api.silae.fr/payroll' as the base URL.|
|Mysolution|`mysolution/default`|[Mysolution's API](https://swagger.mysolution.nl/). We automatically authenticate all requests and use the customer's domain as base URL.|
|InRecruiting by Zucchetti|`inrecruiting/default`|[inRecruiting's v3 API](https://inrecruiting.intervieweb.it/api-docs/). We automatically authenticate all requests and use the customers domain as base URL|
|Connexys By Bullhorn|`connexys/api`|[Connexy's API](https://api.conexsys.com/client/v2/docs/#section/Overview). We automatically authenticate all requests and use `https://\{connexys_domain\}/` as the base URL.|
|HR4YOU|`hr4you/v2`|[HR4YOU's v2 API](https://apiprodemo.hr4you.org/api2/docs). We automatically authenticate all requests and use the customers provided base URL (e.g., https://`\{base_url\}`/ or https://`\{subdomain\}.hr4you.org`/).|
|Cornerstone OnDemand|`cornerstoneondemand/recruiting`|Cornerstone's [Recruiting API](https://csod.dev/reference/recruiting/). We automatically authenticate all requests using the client ID and secret and use `https://your_domain.csod.com/services/api` as the base URL.|
|Zvoove Recruit|`zvooverecruit/jobs`|[Zvoove Recruit's Jobs API](https://api.zvoove.com/docs/). We automatically authenticate all requests using the jobs API key and use 'https://\{domain\}/api/public' as base URL.|
|Zvoove Recruit|`zvooverecruit/applicants`|[Zvoove Recruit's Applicants API](https://api.zvoove.com/docs/). We automatically authenticate all requests using the applicants API key and use 'https://\{domain\}/api/public' as base URL.|
|Spark Hire Recruit|`comeet/api`|[Spark Hire Recruit's API.](https://developers.comeet.com/reference/recruiting-api-overview)We automatically authenticate all requests and use `https://api.comeet.com` as the base URL.|
|Leapsome|`leapsome/scim`|Leapsome [SCIM API](https://api.leapsome.com/scim/v1/api-docs/). We automatically authenticate all requests using the credentials supplied by the customer and use `https://api.leapsome.com/scim/v1` as the base URL.|
|Leapsome|`leapsome/v1`|Leapsome [API](https://api.leapsome.com/v1/api-docs/). We automatically authenticate all requests using the credentials supplied by the customer and use `https://api.leapsome.com/v1` as the base URL.|
|Compleet|`compleetpitcher/pitcher`|Compleet's Pitcher API. We automatically authenticate all requests and use the configured base URL.|
|Gem|`gem/api`|Gem's [ATS API](https://api.gem.com/ats/v0/reference) We automatically authenticate all requests.|
|workforce.com|`workforcecom/api`|Workforce.com [API](https://my.workforce.com/api/v2/documentation). We automatically authenticate all requests using the provided credentials and use `https://my.tanda.co` as the base URL.|
|Laura|`laura/api`|We automatically authenticate all requests and use `https://\{subdomain\}.rekrytointi.com/api/v1.2` as the base URL.|
|Coveto (REST API)|`covetorest/v1`|We automatically use `https://\{subdomain\}.coveto.de/public/api/v1` as the base URL. https://demo.coveto.de/swagger-ui/index.html#/|
|Coveto (legacy SOAP API)|`coveto/public`|We automatically use `https://\{subdomain\}.coveto.de` as the base URL.|
|MHR People First|`peoplefirst/v1`|MHR People First [v1 API](https://docs.people-first.com/api/api-docs/api-docs.html). We automatically authenticate all requests using the access token and tenant/environment codes. For default environments, we use `https://\{tenant_code\}.people-first.com/api/v1` as the base URL. For non-default environments, we use `https://\{tenant_code\}-\{environment_code\}.people-first.com/api/v1`.|
|SD Worx|`sdworx/default`|SD Worx's [OData API](https://apistaging.cobra.sdworx.com/Resources). We automatically authenticate all requests using the client ID and secret and use `\{api_url\}` as the base URL.|
|Crelate|`crelate/api`|Crelate [REST API](https://help.crelate.com/en/articles/4120536-crelate-api-developer-guide). We automatically authenticate all requests and use `https://app.crelate.com/api3` as the base URL.|
|Absence.io|`absenceio/v2`|Absence.io [API](https://docs.absence.io/). We automatically authenticate all requests and use `https://app.absence.io/api/v2` as the base URL.|
|Manatal|`manatal/open-api-v3`|[Manatal's Open API v3](https://developers.manatal.com/reference/getting-started). We automatically authenticate all requests and use `https://api.manatal.com/open/v3` as the base URL.|
|Manatal|`manatal/career-page`|Manatal's Career Page API. We use `https://api.manatal.com/open/v3/career-page/\{client_slug\}` as the base URL.|
|Avionté|`avionte/front-office-v1`|Avionte's API. We automatically authenticate all requests and use `https://api.avionte.com/front-office/v1` as the base URL. Documentation for the BOLD Front Office API: https://developer.avionte.com/reference/get-all-talent-tags|
|a3innuva Nómina|`a3innuvanomina/laboral`|a3innuva Nómina API [docs](https://a3developers.wolterskluwer.es/). Requests are automatically authenticated using OAuth access tokens (refreshed when needed). Base URL: `https://a3api.wolterskluwer.es/Laboral/api`.|
|DATEV|`datevhr/hr-exports`|DATEV's [hr-exports](https://developer.datev.de/en/product-detail/hr-exports/1.0.0/overview). We automatically authenticate all requests and use `https://hr-exports.api.datev.de/\{platform|platform-sandbox\}/v1/clients/\{client-id\}` as the base URL.|
|DATEV|`datevhr/hr:payrollreports`|DATEV's [hr:payrollreports](https://developer.datev.de/en/product-detail/hr-payrollreports/2.0.0/overview) API. We automatically authenticate all requests and use `https://hr-payrollreports.api.datev.de/\{platform|platform-sandbox\}/v1/clients/\{client-id\}/` as the base URL.|
|DATEV|`datevhr/eau`|DATEV's [eau](https://developer.datev.de/en/product-detail/eau-api/1.0.0/overview) API. We automatically authenticate all requests and use `https://eau.api.datev.de/\{platform|platform-sandbox\}/v1/clients/\{client-id\}/` as the base URL.|
|Sympa|`sympa/api`|Sympa's [API](https://documenter.getpostman.com/view/33639379/2sA3kXG1vX#intro). We automatically authenticate all requests and use `https://api.sympahr.net/api/` as the base URL.|
|Breezy HR|`breezyhr/v3`|[BreezyHR's v3 API](https://developer.breezy.hr/reference/overview). We automatically authenticate all requests and use "https://api.breezy.hr/v3/" as the base URL.|
|Flatchr|`flatchr/api`|Flatchr's [API](https://developers.flatchr.io/docs/getting_started). We automatically authenticate all requests and use `https://api.flatchr.io` as the base URL.|
|Flatchr|`flatchr/career`|Flatchr's [Career API](https://developers.flatchr.io/docs/QuickStart/Candidats/Creer_un_candidat). We automatically authenticate all requests and use `https://career.flatchr.io` as the base URL.|
|ApplicantStack|`applicantstack/api`|ApplicantStack's [API](https://helpas.payrollservers.info/s/article/API-Integration-Guide). We automatically authenticate all requests and use `https://\{subdomain\}.applicantstack.com/api/` as the base URL.|
|Visma Raet - Youforce|`youforce/v1.0`|[Youforce's basic v1.0 API](https://vr-api-integration.github.io/youforce-api-documentation/postman_collections.html). We automatically authenticate all requests and use 'https://api.youforce.com' as base URL.|
|PeopleXD|`peoplexd/b2b`|PeopleXD's [B2B API](https://documenter.getpostman.com/view/3101638/TzeTHUDu#intro). We automatically authenticate all requests and use `https://api.corehr.com/ws/\{tenant_id\}/corehr` or `https://uatapi.corehr.com/ws/\{tenant_id\}/corehr` as the base URL.|

<Note>Please note that the passthrough API endpoints are only meant for edge cases. That's why we only expose them for new integrations after understanding a concrete customer use case. If you have such a use case in mind, please reach out to Kombo.</Note>

### Example Usage

<!-- UsageSnippet language="python" operationID="PostPassthroughToolApi" method="post" path="/passthrough/{tool}/{api}" -->
```python
from kombo import Kombo


with Kombo(
    integration_id="workday:HWUTwvyx2wLoSUHphiWVrp28",
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.send_passthrough_request(tool="personio", api="personnel", method="GET", path="/company/employees")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `tool`                                                                                                                                                                               | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The ID of the tool whose passthrough API you want to call (e.g., `personio`).                                                                                                        |
| `api`                                                                                                                                                                                | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The ID of the passthrough API you want to call (some tools provide multiple). Check the endpoint description for a list of all available APIs.                                       |
| `method`                                                                                                                                                                             | [models.Method](../../models/method.md)                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                   | The HTTP method (e.g., `GET`) of the request.                                                                                                                                        |
| `path`                                                                                                                                                                               | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The path of the endpoint you want to call. We automatically prepend the base URL of the API (all base URLs are documented in the endpoint description).                              |
| `headers`                                                                                                                                                                            | Dict[str, *str*]                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | The headers to send with the request. Note that we automatically supply any authentication-related headers.                                                                          |
| `params`                                                                                                                                                                             | Dict[str, *str*]                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | The query parameters to send in addition to the ones in the `path`.                                                                                                                  |
| `data`                                                                                                                                                                               | *Optional[Any]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | The data to submit as part of the request body. This can either be an array or object (in which case we will forward it as JSON) or a string (in which case we will forward it raw). |
| `response_as_base64`                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | If set to `true`, the response will be returned as a base64-encoded string. This is useful for binary data (e.g., PDFs).                                                             |
| `multipart_form_data`                                                                                                                                                                | List[[models.MultipartFormDatum](../../models/multipartformdatum.md)]                                                                                                                | :heavy_minus_sign:                                                                                                                                                                   | N/A                                                                                                                                                                                  |
| `api_options`                                                                                                                                                                        | Dict[str, *str*]                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Custom options interpreted by the passthrough API adapter you've selected. These options are not documented right now as they're only for very advanced use cases.                   |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |

### Response

**[models.PostPassthroughToolAPIPositiveResponse](../../models/postpassthroughtoolapipositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## delete_integration

Delete the specified integration.
**⚠️ This can not be undone!**

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteIntegrationsIntegrationId" method="delete" path="/integrations/{integration_id}" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.delete_integration(integration_id="<id>", body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                                | *str*                                                                                                           | :heavy_check_mark:                                                                                              | DELETE /integrations/:integration_id Parameter                                                                  |
| `body`                                                                                                          | [models.DeleteIntegrationsIntegrationIDRequestBody](../../models/deleteintegrationsintegrationidrequestbody.md) | :heavy_check_mark:                                                                                              | DELETE /integrations/:integration_id Request body                                                               |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.DeleteIntegrationsIntegrationIDPositiveResponse](../../models/deleteintegrationsintegrationidpositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## get_integration_details

Get the specified integration with everything you need to display it to your customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetIntegrationsIntegrationId" method="get" path="/integrations/{integration_id}" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.get_integration_details(integration_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `integration_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | GET /integrations/:integration_id Parameter                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetIntegrationsIntegrationIDPositiveResponse](../../models/getintegrationsintegrationidpositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## create_reconnection_link

Create a link that will allow the user to reconnect an integration. This is useful if you want to allow your users to update the credentials if the old ones for example expired.

Embed this the same way you would [embed the connect link](/connect/embedded-flow). By default, the link will be valid for 1 hour.

### Example Request Body

```json
{
  "language": "en",
  "scope_config_id": "9Pv6aCFwNDEzPNmwjSsY9SQx",
  "link_type": "EMBEDDED"
}
```

### Example Usage

<!-- UsageSnippet language="python" operationID="PostIntegrationsIntegrationIdRelink" method="post" path="/integrations/{integration_id}/relink" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.create_reconnection_link(integration_id="personio:93fCvorjZ2jas7ZekX1V1n5d", language="en", scope_config_id="9Pv6aCFwNDEzPNmwjSsY9SQx", link_type="EMBEDDED")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                       | POST /integrations/:integration_id/relink Parameter                                                                                                                                                                                                                                                                                                                                                                                                      |
| `language`                                                                                                                                                                                                                                                                                                                                                                                                                                               | [OptionalNullable[models.PostIntegrationsIntegrationIDRelinkRequestBodyLanguage]](../../models/postintegrationsintegrationidrelinkrequestbodylanguage.md)                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                       | Language of the connection flow UI.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `scope_config_id`                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                       | Specify a scope config which the integration will start using once the reconnection flow has been completed.<br/><br/>This can be useful if you want to update the permissions of an integration, but only want the change to take effect once the user has updated their API credentials to prevent sync issues.                                                                                                                                        |
| `link_type`                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[models.PostIntegrationsIntegrationIDRelinkRequestBodyLinkType]](../../models/postintegrationsintegrationidrelinkrequestbodylinktype.md)                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                       | The type of link you want to create. `EMBEDDED` is for the [embedded flow](../guides/connect/embedded-flow) using the Kombo Connect SDK (these links are valid for 1 hour) and `MAGIC_LINK` is for [magic links](../guides/connect/magic-links) which you send out manually to customers (there are valid for 1 year).<br/><br/>This defaults to `EMBEDDED`, which is our recommended method of implementing the connection flow for a seamless user experience. |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.PostIntegrationsIntegrationIDRelinkPositiveResponse](../../models/postintegrationsintegrationidrelinkpositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## get_integration_fields

Get all fields available on the specified integration.
**This includes the mapping to your custom fields**

### Example Usage

<!-- UsageSnippet language="python" operationID="GetIntegrationsIntegrationIdIntegrationFields" method="get" path="/integrations/{integration_id}/integration-fields" -->
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

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                                             | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | GET /integrations/:integration_id/integration-fields Parameter                                                               |
| `cursor`                                                                                                                     | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response. |
| `page_size`                                                                                                                  | *Optional[int]*                                                                                                              | :heavy_minus_sign:                                                                                                           | The number of results to return per page. Maximum is 2000.                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.GetIntegrationsIntegrationIDIntegrationFieldsResponse](../../models/getintegrationsintegrationidintegrationfieldsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## update_integration_field

When enabled, the integration field will be passed as part of the `integration_fields` array on the specific model endpoint. Providing false will disable the passthrough for the specified field.

### Example Usage

<!-- UsageSnippet language="python" operationID="PatchIntegrationsIntegrationIdIntegrationFieldsIntegrationFieldId" method="patch" path="/integrations/{integration_id}/integration-fields/{integration_field_id}" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.update_integration_field(integration_id="integration_id", integration_field_id="integration_field_id", enable_passthrough=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `integration_id`                                                                       | *str*                                                                                  | :heavy_check_mark:                                                                     | PATCH /integrations/:integration_id/integration-fields/:integration_field_id Parameter |
| `integration_field_id`                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | PATCH /integrations/:integration_id/integration-fields/:integration_field_id Parameter |
| `enable_passthrough`                                                                   | *Nullable[bool]*                                                                       | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[models.PatchIntegrationsIntegrationIDIntegrationFieldsIntegrationFieldIDPositiveResponse](../../models/patchintegrationsintegrationidintegrationfieldsintegrationfieldidpositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## get_custom_fields

Get all custom fields available on the specified integration.
**This includes the mapping to the corresponding integration field if applicable*

### Example Usage

<!-- UsageSnippet language="python" operationID="GetIntegrationsIntegrationIdCustomFields" method="get" path="/integrations/{integration_id}/custom-fields" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.get_custom_fields(integration_id="<id>", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                                             | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | GET /integrations/:integration_id/custom-fields Parameter                                                                    |
| `cursor`                                                                                                                     | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response. |
| `page_size`                                                                                                                  | *Optional[int]*                                                                                                              | :heavy_minus_sign:                                                                                                           | The number of results to return per page. Maximum is 250.                                                                    |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.GetIntegrationsIntegrationIDCustomFieldsResponse](../../models/getintegrationsintegrationidcustomfieldsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## update_custom_field_mapping

Updates the mapping of a given custom field. If the custom field is already mapped, it will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="PutIntegrationsIntegrationIdCustomFieldsCustomFieldId" method="put" path="/integrations/{integration_id}/custom-fields/{custom_field_id}" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.update_custom_field_mapping(integration_id="integration_id", custom_field_id="custom_field_id", integration_field_id="integration_field_id")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                        | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The unique ID of the integration where the custom field mapping should be updated                       |
| `custom_field_id`                                                                                       | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The unique ID of the custom field that should be updated                                                |
| `integration_field_id`                                                                                  | *Nullable[str]*                                                                                         | :heavy_check_mark:                                                                                      | The integration field's unique ID which the custom field should be mapped to. Null to remove a mapping. |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.PutIntegrationsIntegrationIDCustomFieldsCustomFieldIDPositiveResponse](../../models/putintegrationsintegrationidcustomfieldscustomfieldidpositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |

## get_tools

Get a list of the tools (i.e., integrations) enabled in your environment.
 This can (in combination with the `integration_tool` parameter of [the "Create Link" endpoint](/v1/post-create-link)) be used to, for example, display a custom list or grid of available integrations to your end users instead of exposing Kombo Connect's standard tool selector.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetToolsCategory" method="get" path="/tools/{category}" -->
```python
from kombo import Kombo


with Kombo(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as k_client:

    res = k_client.general.get_tools(category="ats")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `category`                                                                                    | [models.GetToolsCategoryParameterCategory](../../models/gettoolscategoryparametercategory.md) | :heavy_check_mark:                                                                            | GET /tools/:category Parameter                                                                |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.GetToolsCategoryPositiveResponse](../../models/gettoolscategorypositiveresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.KomboGeneralError | default                  | application/json         |
| errors.SDKDefaultError   | 4XX, 5XX                 | \*/\*                    |