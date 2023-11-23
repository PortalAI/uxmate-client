# UpdateBusinessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**business_name** | **str** |  | 
**business_description** | **str** |  | 

## Example

```python
from openapi_client.models.update_business_response import UpdateBusinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBusinessResponse from a JSON string
update_business_response_instance = UpdateBusinessResponse.from_json(json)
# print the JSON string representation of the object
print UpdateBusinessResponse.to_json()

# convert the object into a dict
update_business_response_dict = update_business_response_instance.to_dict()
# create an instance of UpdateBusinessResponse from a dict
update_business_response_form_dict = update_business_response.from_dict(update_business_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


