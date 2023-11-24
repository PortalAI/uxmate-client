# LinksAnyOfValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_ref** | [**Operationref**](Operationref.md) |  | [optional] 
**operation_id** | [**Operationid**](Operationid.md) |  | [optional] 
**parameters** | [**Parameters**](Parameters.md) |  | [optional] 
**request_body** | [**Requestbody**](Requestbody.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**server** | [**LinkServer**](LinkServer.md) |  | [optional] 
**ref** | **object** |  | 

## Example

```python
from uxmate_client.models.links_any_of_value import LinksAnyOfValue

# TODO update the JSON string below
json = "{}"
# create an instance of LinksAnyOfValue from a JSON string
links_any_of_value_instance = LinksAnyOfValue.from_json(json)
# print the JSON string representation of the object
print LinksAnyOfValue.to_json()

# convert the object into a dict
links_any_of_value_dict = links_any_of_value_instance.to_dict()
# create an instance of LinksAnyOfValue from a dict
links_any_of_value_form_dict = links_any_of_value.from_dict(links_any_of_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


