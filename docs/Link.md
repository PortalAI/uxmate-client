# Link


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_ref** | [**Operationref**](Operationref.md) |  | [optional] 
**operation_id** | [**Operationid**](Operationid.md) |  | [optional] 
**parameters** | [**Parameters**](Parameters.md) |  | [optional] 
**request_body** | [**Requestbody**](Requestbody.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**server** | [**LinkServer**](LinkServer.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print Link.to_json()

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_form_dict = link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

