# uxmate_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import uxmate_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import uxmate_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import uxmate_client
from uxmate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = uxmate_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with uxmate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = uxmate_client.DefaultApi(api_client)
    send_new_message_request = uxmate_client.SendNewMessageRequest() # SendNewMessageRequest | 

    try:
        # Chat With Bot
        api_response = api_instance.chat_with_bot_chat_post(send_new_message_request)
        print("The response of DefaultApi->chat_with_bot_chat_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->chat_with_bot_chat_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**chat_with_bot_chat_post**](docs/DefaultApi.md#chat_with_bot_chat_post) | **POST** /chat/ | Chat With Bot
*DefaultApi* | [**create_business_and_survey_business_and_survey_post**](docs/DefaultApi.md#create_business_and_survey_business_and_survey_post) | **POST** /business_and_survey/ | Create Business And Survey
*DefaultApi* | [**create_business_business_post**](docs/DefaultApi.md#create_business_business_post) | **POST** /business/ | Create Business
*DefaultApi* | [**create_survey_survey_post**](docs/DefaultApi.md#create_survey_survey_post) | **POST** /survey/ | Create Survey
*DefaultApi* | [**create_template_template_post**](docs/DefaultApi.md#create_template_template_post) | **POST** /template/ | Create Template
*DefaultApi* | [**delete_business**](docs/DefaultApi.md#delete_business) | **DELETE** /business/{business_id} | Delete Business
*DefaultApi* | [**delete_survey**](docs/DefaultApi.md#delete_survey) | **DELETE** /survey/{survey_id} | Delete Survey
*DefaultApi* | [**delete_survey_record**](docs/DefaultApi.md#delete_survey_record) | **DELETE** /survey_record/{record_id} | Delete Survey Record
*DefaultApi* | [**get_business_business_business_id_get**](docs/DefaultApi.md#get_business_business_business_id_get) | **GET** /business/{business_id} | Get Business
*DefaultApi* | [**get_businesses_business_get**](docs/DefaultApi.md#get_businesses_business_get) | **GET** /business | Get Businesses
*DefaultApi* | [**get_chat_history_chat_history_record_id_get**](docs/DefaultApi.md#get_chat_history_chat_history_record_id_get) | **GET** /chat_history/{record_id} | Get Chat History
*DefaultApi* | [**get_create_survey_record_survey_record_post**](docs/DefaultApi.md#get_create_survey_record_survey_record_post) | **POST** /survey_record/ | Get Create Survey Record
*DefaultApi* | [**get_survey_insight_survey_survey_id_insight_get**](docs/DefaultApi.md#get_survey_insight_survey_survey_id_insight_get) | **GET** /survey/{survey_id}/insight | Get Survey Insight
*DefaultApi* | [**get_survey_record_survey_record_record_id_get**](docs/DefaultApi.md#get_survey_record_survey_record_record_id_get) | **GET** /survey_record/{record_id} | Get Survey Record
*DefaultApi* | [**get_survey_summary_survey_record_record_id_summary_get**](docs/DefaultApi.md#get_survey_summary_survey_record_record_id_summary_get) | **GET** /survey_record/{record_id}/summary | Get Survey Summary
*DefaultApi* | [**get_survey_survey_survey_id_get**](docs/DefaultApi.md#get_survey_survey_survey_id_get) | **GET** /survey/{survey_id} | Get Survey
*DefaultApi* | [**get_survey_xlsx_survey_survey_id_report_xlsx_get**](docs/DefaultApi.md#get_survey_xlsx_survey_survey_id_report_xlsx_get) | **GET** /survey/{survey_id}/report/xlsx | Get Survey Xlsx
*DefaultApi* | [**get_surveys**](docs/DefaultApi.md#get_surveys) | **GET** /survey | Get Surveys
*DefaultApi* | [**get_surveys_list_by_business_id_business_business_id_survey_get**](docs/DefaultApi.md#get_surveys_list_by_business_id_business_business_id_survey_get) | **GET** /business/{business_id}/survey | Get Surveys List By Business Id
*DefaultApi* | [**get_template_by_survey_id_survey_survey_id_template_get**](docs/DefaultApi.md#get_template_by_survey_id_survey_survey_id_template_get) | **GET** /survey/{survey_id}/template | Get Template By Survey Id
*DefaultApi* | [**get_template_template_template_id_get**](docs/DefaultApi.md#get_template_template_template_id_get) | **GET** /template/{template_id} | Get Template
*DefaultApi* | [**health_check_health_check_get**](docs/DefaultApi.md#health_check_health_check_get) | **GET** /health_check | Health Check
*DefaultApi* | [**init_survey_insight_survey_survey_id_insight_new_put**](docs/DefaultApi.md#init_survey_insight_survey_survey_id_insight_new_put) | **PUT** /survey/{survey_id}/insight/new | Init Survey Insight
*DefaultApi* | [**init_survey_summary_survey_record_record_id_summary_new_put**](docs/DefaultApi.md#init_survey_summary_survey_record_record_id_summary_new_put) | **PUT** /survey_record/{record_id}/summary/new | Init Survey Summary
*DefaultApi* | [**list_survey_records_survey_survey_id_records_get**](docs/DefaultApi.md#list_survey_records_survey_survey_id_records_get) | **GET** /survey/{survey_id}/records | List Survey Records
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Root
*DefaultApi* | [**update_business_business_put**](docs/DefaultApi.md#update_business_business_put) | **PUT** /business/ | Update Business
*DefaultApi* | [**update_survey**](docs/DefaultApi.md#update_survey) | **PUT** /survey/{survey_id} | Update Survey
*DefaultApi* | [**update_template_template_put**](docs/DefaultApi.md#update_template_template_put) | **PUT** /template/ | Update Template


## Documentation For Models

 - [Additionalproperties](docs/Additionalproperties.md)
 - [Allof](docs/Allof.md)
 - [Allowreserved](docs/Allowreserved.md)
 - [Anchor](docs/Anchor.md)
 - [Anyof](docs/Anyof.md)
 - [Attribute](docs/Attribute.md)
 - [ChatHistory](docs/ChatHistory.md)
 - [Comment](docs/Comment.md)
 - [Const](docs/Const.md)
 - [Contains](docs/Contains.md)
 - [Content](docs/Content.md)
 - [Contentencoding](docs/Contentencoding.md)
 - [Contentmediatype](docs/Contentmediatype.md)
 - [Contentschema](docs/Contentschema.md)
 - [Contenttype](docs/Contenttype.md)
 - [CreateBusinessAndSurveyRequest](docs/CreateBusinessAndSurveyRequest.md)
 - [CreateBusinessAndSurveyResponse](docs/CreateBusinessAndSurveyResponse.md)
 - [CreateBusinessRequest](docs/CreateBusinessRequest.md)
 - [CreateBusinessResponse](docs/CreateBusinessResponse.md)
 - [CreateSurveyRequest](docs/CreateSurveyRequest.md)
 - [CreateSurveyResponse](docs/CreateSurveyResponse.md)
 - [CreateTemplateRequest](docs/CreateTemplateRequest.md)
 - [CreateTemplateResponse](docs/CreateTemplateResponse.md)
 - [Default](docs/Default.md)
 - [Defs](docs/Defs.md)
 - [DefsAnyOfValue](docs/DefsAnyOfValue.md)
 - [Dependentrequired](docs/Dependentrequired.md)
 - [Dependentschemas](docs/Dependentschemas.md)
 - [Deprecated](docs/Deprecated.md)
 - [Description](docs/Description.md)
 - [Discriminator](docs/Discriminator.md)
 - [Dynamicanchor](docs/Dynamicanchor.md)
 - [Dynamicref](docs/Dynamicref.md)
 - [Encoding](docs/Encoding.md)
 - [Encoding1](docs/Encoding1.md)
 - [Enum](docs/Enum.md)
 - [Enum1](docs/Enum1.md)
 - [Example](docs/Example.md)
 - [Example1](docs/Example1.md)
 - [Examples](docs/Examples.md)
 - [Examples1](docs/Examples1.md)
 - [ExamplesAnyOfValue](docs/ExamplesAnyOfValue.md)
 - [Exclusivemaximum](docs/Exclusivemaximum.md)
 - [Exclusiveminimum](docs/Exclusiveminimum.md)
 - [Explode](docs/Explode.md)
 - [ExternalDocumentation](docs/ExternalDocumentation.md)
 - [Externalvalue](docs/Externalvalue.md)
 - [Format](docs/Format.md)
 - [GetBusinessListResponse](docs/GetBusinessListResponse.md)
 - [GetBusinessResponse](docs/GetBusinessResponse.md)
 - [GetChatHistoryResponse](docs/GetChatHistoryResponse.md)
 - [GetOrCreateSurveyRecordRequest](docs/GetOrCreateSurveyRecordRequest.md)
 - [GetOrCreateSurveyRecordResponse](docs/GetOrCreateSurveyRecordResponse.md)
 - [GetSurveyInsightResponse](docs/GetSurveyInsightResponse.md)
 - [GetSurveyRecordResponse](docs/GetSurveyRecordResponse.md)
 - [GetSurveyRecordSummaryResponse](docs/GetSurveyRecordSummaryResponse.md)
 - [GetSurveyResponse](docs/GetSurveyResponse.md)
 - [GetTemplateResponse](docs/GetTemplateResponse.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Header](docs/Header.md)
 - [Headers](docs/Headers.md)
 - [HeadersAnyOfValue](docs/HeadersAnyOfValue.md)
 - [Id](docs/Id.md)
 - [Items](docs/Items.md)
 - [Link](docs/Link.md)
 - [LinkServer](docs/LinkServer.md)
 - [Links](docs/Links.md)
 - [LinksAnyOfValue](docs/LinksAnyOfValue.md)
 - [ListSurveyRecordsResponse](docs/ListSurveyRecordsResponse.md)
 - [ListSurveysByBusinessResponse](docs/ListSurveysByBusinessResponse.md)
 - [ListSurveysResponse](docs/ListSurveysResponse.md)
 - [Maxcontains](docs/Maxcontains.md)
 - [Maximum](docs/Maximum.md)
 - [Maxitems](docs/Maxitems.md)
 - [Maxlength](docs/Maxlength.md)
 - [Maxproperties](docs/Maxproperties.md)
 - [MediaType](docs/MediaType.md)
 - [Message](docs/Message.md)
 - [Mincontains](docs/Mincontains.md)
 - [Minimum](docs/Minimum.md)
 - [Minitems](docs/Minitems.md)
 - [Minlength](docs/Minlength.md)
 - [Minproperties](docs/Minproperties.md)
 - [ModelElse](docs/ModelElse.md)
 - [ModelIf](docs/ModelIf.md)
 - [ModelNot](docs/ModelNot.md)
 - [ModelSchema](docs/ModelSchema.md)
 - [Multipleof](docs/Multipleof.md)
 - [Name](docs/Name.md)
 - [Namespace](docs/Namespace.md)
 - [Oneof](docs/Oneof.md)
 - [Operationid](docs/Operationid.md)
 - [Operationref](docs/Operationref.md)
 - [Parameters](docs/Parameters.md)
 - [ParametersAnyOfValue](docs/ParametersAnyOfValue.md)
 - [Pattern](docs/Pattern.md)
 - [Patternproperties](docs/Patternproperties.md)
 - [Prefix](docs/Prefix.md)
 - [Prefixitems](docs/Prefixitems.md)
 - [Properties](docs/Properties.md)
 - [Propertynames](docs/Propertynames.md)
 - [Readonly](docs/Readonly.md)
 - [Ref](docs/Ref.md)
 - [Reference](docs/Reference.md)
 - [Requestbody](docs/Requestbody.md)
 - [Required](docs/Required.md)
 - [Required1](docs/Required1.md)
 - [Response](docs/Response.md)
 - [RoleEnum](docs/RoleEnum.md)
 - [Schema1](docs/Schema1.md)
 - [SchemaDiscriminator](docs/SchemaDiscriminator.md)
 - [SchemaExternalDocs](docs/SchemaExternalDocs.md)
 - [SchemaXml](docs/SchemaXml.md)
 - [SendNewMessageRequest](docs/SendNewMessageRequest.md)
 - [SendNewMessageResponse](docs/SendNewMessageResponse.md)
 - [Server](docs/Server.md)
 - [ServerVariable](docs/ServerVariable.md)
 - [Style](docs/Style.md)
 - [Summary](docs/Summary.md)
 - [SurveyRecord](docs/SurveyRecord.md)
 - [SurveyRecordState](docs/SurveyRecordState.md)
 - [Then](docs/Then.md)
 - [Title](docs/Title.md)
 - [Type](docs/Type.md)
 - [Unevaluateditems](docs/Unevaluateditems.md)
 - [Unevaluatedproperties](docs/Unevaluatedproperties.md)
 - [Uniqueitems](docs/Uniqueitems.md)
 - [UpdateBusinessRequest](docs/UpdateBusinessRequest.md)
 - [UpdateBusinessResponse](docs/UpdateBusinessResponse.md)
 - [UpdateSurveyRequest](docs/UpdateSurveyRequest.md)
 - [UpdateSurveyResponse](docs/UpdateSurveyResponse.md)
 - [UpdateTemplateRequest](docs/UpdateTemplateRequest.md)
 - [UpdateTemplateResponse](docs/UpdateTemplateResponse.md)
 - [Url](docs/Url.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [Value](docs/Value.md)
 - [Variables](docs/Variables.md)
 - [Vocabulary](docs/Vocabulary.md)
 - [Wrapped](docs/Wrapped.md)
 - [Writeonly](docs/Writeonly.md)
 - [XML](docs/XML.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




