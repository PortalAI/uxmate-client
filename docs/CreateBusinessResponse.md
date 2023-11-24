# CreateBusinessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**business_name** | **str** |  | 
**business_description** | **str** |  | 

## Example

```python
from uxmate_client.models.create_business_response import CreateBusinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBusinessResponse from a JSON string
create_business_response_instance = CreateBusinessResponse.from_json(json)
# print the JSON string representation of the object
print CreateBusinessResponse.to_json()

# convert the object into a dict
create_business_response_dict = create_business_response_instance.to_dict()
# create an instance of CreateBusinessResponse from a dict
create_business_response_form_dict = create_business_response.from_dict(create_business_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


