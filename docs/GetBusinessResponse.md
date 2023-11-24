# GetBusinessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**business_name** | **str** |  | 
**business_description** | **str** |  | 

## Example

```python
from uxmate_client.uxmate_client.get_business_response import GetBusinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessResponse from a JSON string
get_business_response_instance = GetBusinessResponse.from_json(json)
# print the JSON string representation of the object
print GetBusinessResponse.to_json()

# convert the object into a dict
get_business_response_dict = get_business_response_instance.to_dict()
# create an instance of GetBusinessResponse from a dict
get_business_response_form_dict = get_business_response.from_dict(get_business_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


