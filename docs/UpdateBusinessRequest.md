# UpdateBusinessRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**business_name** | **str** |  | 
**business_description** | **str** |  | 

## Example

```python
from uxmate_client.models.update_business_request import UpdateBusinessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBusinessRequest from a JSON string
update_business_request_instance = UpdateBusinessRequest.from_json(json)
# print the JSON string representation of the object
print UpdateBusinessRequest.to_json()

# convert the object into a dict
update_business_request_dict = update_business_request_instance.to_dict()
# create an instance of UpdateBusinessRequest from a dict
update_business_request_form_dict = update_business_request.from_dict(update_business_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


