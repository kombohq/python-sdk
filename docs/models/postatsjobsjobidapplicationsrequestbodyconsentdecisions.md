# PostAtsJobsJobIDApplicationsRequestBodyConsentDecisions

The consent decisions for the candidate. SmartRecruiters supports two consent models: 'Single' (use the `SINGLE` key) and 'Separated' (use `SMART_RECRUIT`, `SMART_CRM`, `SMART_MESSAGE_SMS`, and/or `SMART_MESSAGE_WHATSAPP` keys). When this field is provided, it takes precedence over the `gdpr_consent` field for the `consentDecisions` property. See: https://developers.smartrecruiters.com/docs/partners-post-an-application


## Fields

| Field                    | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `single`                 | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |
| `smart_recruit`          | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |
| `smart_crm`              | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |
| `smart_message_sms`      | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |
| `smart_message_whatsapp` | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |