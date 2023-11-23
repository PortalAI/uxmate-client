# GetBusinessListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businesses** | [**List[GetBusinessResponse]**](GetBusinessResponse.md) |  | 

## Example

```python
from openapi_client.models.get_business_list_response import GetBusinessListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessListResponse from a JSON string
get_business_list_response_instance = GetBusinessListResponse.from_json(json)
# print the JSON string representation of the object
print GetBusinessListResponse.to_json()

# convert the object into a dict
get_business_list_response_dict = get_business_list_response_instance.to_dict()
# create an instance of GetBusinessListResponse from a dict
get_business_list_response_form_dict = get_business_list_response.from_dict(get_business_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


