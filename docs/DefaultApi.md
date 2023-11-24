# uxmate_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_with_bot_chat_post**](DefaultApi.md#chat_with_bot_chat_post) | **POST** /chat/ | Chat With Bot
[**create_business_and_survey_business_and_survey_post**](DefaultApi.md#create_business_and_survey_business_and_survey_post) | **POST** /business_and_survey/ | Create Business And Survey
[**create_business_business_post**](DefaultApi.md#create_business_business_post) | **POST** /business/ | Create Business
[**create_survey_survey_post**](DefaultApi.md#create_survey_survey_post) | **POST** /survey/ | Create Survey
[**create_template_template_post**](DefaultApi.md#create_template_template_post) | **POST** /template/ | Create Template
[**delete_business**](DefaultApi.md#delete_business) | **DELETE** /business/{business_id} | Delete Business
[**delete_survey**](DefaultApi.md#delete_survey) | **DELETE** /survey/{survey_id} | Delete Survey
[**delete_survey_record**](DefaultApi.md#delete_survey_record) | **DELETE** /survey_record/{record_id} | Delete Survey Record
[**get_business_business_business_id_get**](DefaultApi.md#get_business_business_business_id_get) | **GET** /business/{business_id} | Get Business
[**get_businesses_business_get**](DefaultApi.md#get_businesses_business_get) | **GET** /business | Get Businesses
[**get_chat_history_chat_history_record_id_get**](DefaultApi.md#get_chat_history_chat_history_record_id_get) | **GET** /chat_history/{record_id} | Get Chat History
[**get_create_survey_record_survey_record_post**](DefaultApi.md#get_create_survey_record_survey_record_post) | **POST** /survey_record/ | Get Create Survey Record
[**get_survey_insight_survey_survey_id_insight_get**](DefaultApi.md#get_survey_insight_survey_survey_id_insight_get) | **GET** /survey/{survey_id}/insight | Get Survey Insight
[**get_survey_record_survey_record_record_id_get**](DefaultApi.md#get_survey_record_survey_record_record_id_get) | **GET** /survey_record/{record_id} | Get Survey Record
[**get_survey_summary_survey_record_record_id_summary_get**](DefaultApi.md#get_survey_summary_survey_record_record_id_summary_get) | **GET** /survey_record/{record_id}/summary | Get Survey Summary
[**get_survey_survey_survey_id_get**](DefaultApi.md#get_survey_survey_survey_id_get) | **GET** /survey/{survey_id} | Get Survey
[**get_survey_xlsx_survey_survey_id_report_xlsx_get**](DefaultApi.md#get_survey_xlsx_survey_survey_id_report_xlsx_get) | **GET** /survey/{survey_id}/report/xlsx | Get Survey Xlsx
[**get_surveys**](DefaultApi.md#get_surveys) | **GET** /survey | Get Surveys
[**get_surveys_list_by_business_id_business_business_id_survey_get**](DefaultApi.md#get_surveys_list_by_business_id_business_business_id_survey_get) | **GET** /business/{business_id}/survey | Get Surveys List By Business Id
[**get_template_by_survey_id_survey_survey_id_template_get**](DefaultApi.md#get_template_by_survey_id_survey_survey_id_template_get) | **GET** /survey/{survey_id}/template | Get Template By Survey Id
[**get_template_template_template_id_get**](DefaultApi.md#get_template_template_template_id_get) | **GET** /template/{template_id} | Get Template
[**health_check_health_check_get**](DefaultApi.md#health_check_health_check_get) | **GET** /health_check | Health Check
[**init_survey_insight_survey_survey_id_insight_new_put**](DefaultApi.md#init_survey_insight_survey_survey_id_insight_new_put) | **PUT** /survey/{survey_id}/insight/new | Init Survey Insight
[**init_survey_summary_survey_record_record_id_summary_new_put**](DefaultApi.md#init_survey_summary_survey_record_record_id_summary_new_put) | **PUT** /survey_record/{record_id}/summary/new | Init Survey Summary
[**list_survey_records_survey_survey_id_records_get**](DefaultApi.md#list_survey_records_survey_survey_id_records_get) | **GET** /survey/{survey_id}/records | List Survey Records
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**update_business_business_put**](DefaultApi.md#update_business_business_put) | **PUT** /business/ | Update Business
[**update_survey**](DefaultApi.md#update_survey) | **PUT** /survey/{survey_id} | Update Survey
[**update_template_template_put**](DefaultApi.md#update_template_template_put) | **PUT** /template/ | Update Template


# **chat_with_bot_chat_post**
> SendNewMessageResponse chat_with_bot_chat_post(send_new_message_request)

Chat With Bot

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.send_new_message_request import SendNewMessageRequest
from uxmate_client.models.send_new_message_response import SendNewMessageResponse
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
    except Exception as e:
        print("Exception when calling DefaultApi->chat_with_bot_chat_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_new_message_request** | [**SendNewMessageRequest**](SendNewMessageRequest.md)|  | 

### Return type

[**SendNewMessageResponse**](SendNewMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_business_and_survey_business_and_survey_post**
> CreateBusinessAndSurveyResponse create_business_and_survey_business_and_survey_post(create_business_and_survey_request)

Create Business And Survey

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.create_business_and_survey_request import CreateBusinessAndSurveyRequest
from uxmate_client.models.create_business_and_survey_response import CreateBusinessAndSurveyResponse
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
    create_business_and_survey_request = uxmate_client.CreateBusinessAndSurveyRequest() # CreateBusinessAndSurveyRequest | 

    try:
        # Create Business And Survey
        api_response = api_instance.create_business_and_survey_business_and_survey_post(create_business_and_survey_request)
        print("The response of DefaultApi->create_business_and_survey_business_and_survey_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_business_and_survey_business_and_survey_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_business_and_survey_request** | [**CreateBusinessAndSurveyRequest**](CreateBusinessAndSurveyRequest.md)|  | 

### Return type

[**CreateBusinessAndSurveyResponse**](CreateBusinessAndSurveyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_business_business_post**
> CreateBusinessResponse create_business_business_post(create_business_request)

Create Business

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.create_business_request import CreateBusinessRequest
from uxmate_client.models.create_business_response import CreateBusinessResponse
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
    create_business_request = uxmate_client.CreateBusinessRequest() # CreateBusinessRequest | 

    try:
        # Create Business
        api_response = api_instance.create_business_business_post(create_business_request)
        print("The response of DefaultApi->create_business_business_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_business_business_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_business_request** | [**CreateBusinessRequest**](CreateBusinessRequest.md)|  | 

### Return type

[**CreateBusinessResponse**](CreateBusinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_survey_survey_post**
> CreateSurveyResponse create_survey_survey_post(create_survey_request)

Create Survey

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.create_survey_request import CreateSurveyRequest
from uxmate_client.models.create_survey_response import CreateSurveyResponse
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
    create_survey_request = uxmate_client.CreateSurveyRequest() # CreateSurveyRequest | 

    try:
        # Create Survey
        api_response = api_instance.create_survey_survey_post(create_survey_request)
        print("The response of DefaultApi->create_survey_survey_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_survey_survey_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_survey_request** | [**CreateSurveyRequest**](CreateSurveyRequest.md)|  | 

### Return type

[**CreateSurveyResponse**](CreateSurveyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_template_post**
> CreateTemplateResponse create_template_template_post(create_template_request)

Create Template

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.create_template_request import CreateTemplateRequest
from uxmate_client.models.create_template_response import CreateTemplateResponse
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
    create_template_request = uxmate_client.CreateTemplateRequest() # CreateTemplateRequest | 

    try:
        # Create Template
        api_response = api_instance.create_template_template_post(create_template_request)
        print("The response of DefaultApi->create_template_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_template_template_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**CreateTemplateResponse**](CreateTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business**
> Response delete_business(business_id)

Delete Business

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.response import Response
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
    business_id = 'business_id_example' # str | 

    try:
        # Delete Business
        api_response = api_instance.delete_business(business_id)
        print("The response of DefaultApi->delete_business:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_business: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_survey**
> Response delete_survey(survey_id)

Delete Survey

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.response import Response
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
    survey_id = 'survey_id_example' # str | 

    try:
        # Delete Survey
        api_response = api_instance.delete_survey(survey_id)
        print("The response of DefaultApi->delete_survey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_survey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_survey_record**
> Response delete_survey_record(record_id)

Delete Survey Record

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.response import Response
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
    record_id = 'record_id_example' # str | 

    try:
        # Delete Survey Record
        api_response = api_instance.delete_survey_record(record_id)
        print("The response of DefaultApi->delete_survey_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_survey_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_business_business_id_get**
> GetBusinessResponse get_business_business_business_id_get(business_id)

Get Business

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_business_response import GetBusinessResponse
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
    business_id = 'business_id_example' # str | 

    try:
        # Get Business
        api_response = api_instance.get_business_business_business_id_get(business_id)
        print("The response of DefaultApi->get_business_business_business_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_business_business_business_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 

### Return type

[**GetBusinessResponse**](GetBusinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_businesses_business_get**
> GetBusinessListResponse get_businesses_business_get()

Get Businesses

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_business_list_response import GetBusinessListResponse
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

    try:
        # Get Businesses
        api_response = api_instance.get_businesses_business_get()
        print("The response of DefaultApi->get_businesses_business_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_businesses_business_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBusinessListResponse**](GetBusinessListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_history_chat_history_record_id_get**
> GetChatHistoryResponse get_chat_history_chat_history_record_id_get(record_id)

Get Chat History

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_chat_history_response import GetChatHistoryResponse
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
    record_id = 'record_id_example' # str | 

    try:
        # Get Chat History
        api_response = api_instance.get_chat_history_chat_history_record_id_get(record_id)
        print("The response of DefaultApi->get_chat_history_chat_history_record_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_chat_history_chat_history_record_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 

### Return type

[**GetChatHistoryResponse**](GetChatHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_create_survey_record_survey_record_post**
> GetOrCreateSurveyRecordResponse get_create_survey_record_survey_record_post(get_or_create_survey_record_request)

Get Create Survey Record

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_or_create_survey_record_request import GetOrCreateSurveyRecordRequest
from uxmate_client.models.get_or_create_survey_record_response import GetOrCreateSurveyRecordResponse
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
    get_or_create_survey_record_request = uxmate_client.GetOrCreateSurveyRecordRequest() # GetOrCreateSurveyRecordRequest | 

    try:
        # Get Create Survey Record
        api_response = api_instance.get_create_survey_record_survey_record_post(get_or_create_survey_record_request)
        print("The response of DefaultApi->get_create_survey_record_survey_record_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_create_survey_record_survey_record_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_or_create_survey_record_request** | [**GetOrCreateSurveyRecordRequest**](GetOrCreateSurveyRecordRequest.md)|  | 

### Return type

[**GetOrCreateSurveyRecordResponse**](GetOrCreateSurveyRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_insight_survey_survey_id_insight_get**
> GetSurveyInsightResponse get_survey_insight_survey_survey_id_insight_get(survey_id)

Get Survey Insight

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_survey_insight_response import GetSurveyInsightResponse
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
    survey_id = 'survey_id_example' # str | 

    try:
        # Get Survey Insight
        api_response = api_instance.get_survey_insight_survey_survey_id_insight_get(survey_id)
        print("The response of DefaultApi->get_survey_insight_survey_survey_id_insight_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_survey_insight_survey_survey_id_insight_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

[**GetSurveyInsightResponse**](GetSurveyInsightResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_record_survey_record_record_id_get**
> GetSurveyRecordResponse get_survey_record_survey_record_record_id_get(record_id)

Get Survey Record

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_survey_record_response import GetSurveyRecordResponse
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
    record_id = 'record_id_example' # str | 

    try:
        # Get Survey Record
        api_response = api_instance.get_survey_record_survey_record_record_id_get(record_id)
        print("The response of DefaultApi->get_survey_record_survey_record_record_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_survey_record_survey_record_record_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 

### Return type

[**GetSurveyRecordResponse**](GetSurveyRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_summary_survey_record_record_id_summary_get**
> GetSurveyRecordSummaryResponse get_survey_summary_survey_record_record_id_summary_get(record_id)

Get Survey Summary

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_survey_record_summary_response import GetSurveyRecordSummaryResponse
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
    record_id = 'record_id_example' # str | 

    try:
        # Get Survey Summary
        api_response = api_instance.get_survey_summary_survey_record_record_id_summary_get(record_id)
        print("The response of DefaultApi->get_survey_summary_survey_record_record_id_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_survey_summary_survey_record_record_id_summary_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 

### Return type

[**GetSurveyRecordSummaryResponse**](GetSurveyRecordSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_survey_survey_id_get**
> GetSurveyResponse get_survey_survey_survey_id_get(survey_id)

Get Survey

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_survey_response import GetSurveyResponse
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
    survey_id = 'survey_id_example' # str | 

    try:
        # Get Survey
        api_response = api_instance.get_survey_survey_survey_id_get(survey_id)
        print("The response of DefaultApi->get_survey_survey_survey_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_survey_survey_survey_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

[**GetSurveyResponse**](GetSurveyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_xlsx_survey_survey_id_report_xlsx_get**
> get_survey_xlsx_survey_survey_id_report_xlsx_get(survey_id)

Get Survey Xlsx

### Example

```python
import time
import os
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
    survey_id = 'survey_id_example' # str | 

    try:
        # Get Survey Xlsx
        api_instance.get_survey_xlsx_survey_survey_id_report_xlsx_get(survey_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_survey_xlsx_survey_survey_id_report_xlsx_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surveys**
> ListSurveysResponse get_surveys()

Get Surveys

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.list_surveys_response import ListSurveysResponse
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

    try:
        # Get Surveys
        api_response = api_instance.get_surveys()
        print("The response of DefaultApi->get_surveys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_surveys: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSurveysResponse**](ListSurveysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surveys_list_by_business_id_business_business_id_survey_get**
> ListSurveysByBusinessResponse get_surveys_list_by_business_id_business_business_id_survey_get(business_id)

Get Surveys List By Business Id

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.list_surveys_by_business_response import ListSurveysByBusinessResponse
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
    business_id = 'business_id_example' # str | 

    try:
        # Get Surveys List By Business Id
        api_response = api_instance.get_surveys_list_by_business_id_business_business_id_survey_get(business_id)
        print("The response of DefaultApi->get_surveys_list_by_business_id_business_business_id_survey_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_surveys_list_by_business_id_business_business_id_survey_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 

### Return type

[**ListSurveysByBusinessResponse**](ListSurveysByBusinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_by_survey_id_survey_survey_id_template_get**
> GetTemplateResponse get_template_by_survey_id_survey_survey_id_template_get(survey_id)

Get Template By Survey Id

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_template_response import GetTemplateResponse
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
    survey_id = 'survey_id_example' # str | 

    try:
        # Get Template By Survey Id
        api_response = api_instance.get_template_by_survey_id_survey_survey_id_template_get(survey_id)
        print("The response of DefaultApi->get_template_by_survey_id_survey_survey_id_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_template_by_survey_id_survey_survey_id_template_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

[**GetTemplateResponse**](GetTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_template_template_id_get**
> GetTemplateResponse get_template_template_template_id_get(template_id)

Get Template

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_template_response import GetTemplateResponse
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
    template_id = 'template_id_example' # str | 

    try:
        # Get Template
        api_response = api_instance.get_template_template_template_id_get(template_id)
        print("The response of DefaultApi->get_template_template_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_template_template_template_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**GetTemplateResponse**](GetTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_health_check_get**
> health_check_health_check_get()

Health Check

### Example

```python
import time
import os
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

    try:
        # Health Check
        api_instance.health_check_health_check_get()
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_health_check_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_survey_insight_survey_survey_id_insight_new_put**
> GetSurveyInsightResponse init_survey_insight_survey_survey_id_insight_new_put(survey_id)

Init Survey Insight

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_survey_insight_response import GetSurveyInsightResponse
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
    survey_id = 'survey_id_example' # str | 

    try:
        # Init Survey Insight
        api_response = api_instance.init_survey_insight_survey_survey_id_insight_new_put(survey_id)
        print("The response of DefaultApi->init_survey_insight_survey_survey_id_insight_new_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->init_survey_insight_survey_survey_id_insight_new_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

[**GetSurveyInsightResponse**](GetSurveyInsightResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_survey_summary_survey_record_record_id_summary_new_put**
> GetSurveyRecordSummaryResponse init_survey_summary_survey_record_record_id_summary_new_put(record_id)

Init Survey Summary

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.get_survey_record_summary_response import GetSurveyRecordSummaryResponse
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
    record_id = 'record_id_example' # str | 

    try:
        # Init Survey Summary
        api_response = api_instance.init_survey_summary_survey_record_record_id_summary_new_put(record_id)
        print("The response of DefaultApi->init_survey_summary_survey_record_record_id_summary_new_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->init_survey_summary_survey_record_record_id_summary_new_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 

### Return type

[**GetSurveyRecordSummaryResponse**](GetSurveyRecordSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_survey_records_survey_survey_id_records_get**
> ListSurveyRecordsResponse list_survey_records_survey_survey_id_records_get(survey_id)

List Survey Records

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.list_survey_records_response import ListSurveyRecordsResponse
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
    survey_id = 'survey_id_example' # str | 

    try:
        # List Survey Records
        api_response = api_instance.list_survey_records_survey_survey_id_records_get(survey_id)
        print("The response of DefaultApi->list_survey_records_survey_survey_id_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_survey_records_survey_survey_id_records_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 

### Return type

[**ListSurveyRecordsResponse**](ListSurveyRecordsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> root_get()

Root

### Example

```python
import time
import os
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

    try:
        # Root
        api_instance.root_get()
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_business_put**
> UpdateBusinessResponse update_business_business_put(update_business_request)

Update Business

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.update_business_request import UpdateBusinessRequest
from uxmate_client.models.update_business_response import UpdateBusinessResponse
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
    update_business_request = uxmate_client.UpdateBusinessRequest() # UpdateBusinessRequest | 

    try:
        # Update Business
        api_response = api_instance.update_business_business_put(update_business_request)
        print("The response of DefaultApi->update_business_business_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_business_business_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_business_request** | [**UpdateBusinessRequest**](UpdateBusinessRequest.md)|  | 

### Return type

[**UpdateBusinessResponse**](UpdateBusinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_survey**
> UpdateSurveyResponse update_survey(survey_id, update_survey_request)

Update Survey

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.update_survey_request import UpdateSurveyRequest
from uxmate_client.models.update_survey_response import UpdateSurveyResponse
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
    survey_id = 'survey_id_example' # str | 
    update_survey_request = uxmate_client.UpdateSurveyRequest() # UpdateSurveyRequest | 

    try:
        # Update Survey
        api_response = api_instance.update_survey(survey_id, update_survey_request)
        print("The response of DefaultApi->update_survey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_survey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **str**|  | 
 **update_survey_request** | [**UpdateSurveyRequest**](UpdateSurveyRequest.md)|  | 

### Return type

[**UpdateSurveyResponse**](UpdateSurveyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_template_put**
> UpdateTemplateResponse update_template_template_put(update_template_request)

Update Template

### Example

```python
import time
import os
import uxmate_client
from uxmate_client.models.update_template_request import UpdateTemplateRequest
from uxmate_client.models.update_template_response import UpdateTemplateResponse
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
    update_template_request = uxmate_client.UpdateTemplateRequest() # UpdateTemplateRequest | 

    try:
        # Update Template
        api_response = api_instance.update_template_template_put(update_template_request)
        print("The response of DefaultApi->update_template_template_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_template_template_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template_request** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)|  | 

### Return type

[**UpdateTemplateResponse**](UpdateTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

