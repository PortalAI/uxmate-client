# uxmate_client.TestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agents_test_metrics_get**](TestApi.md#get_agents_test_metrics_get) | **GET** /test/metrics | Get Agents


# **get_agents_test_metrics_get**
> str get_agents_test_metrics_get()

Get Agents

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
    api_instance = uxmate_client.TestApi(api_client)

    try:
        # Get Agents
        api_response = api_instance.get_agents_test_metrics_get()
        print("The response of TestApi->get_agents_test_metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->get_agents_test_metrics_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

