# ServerVariable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum** | [**Enum1**](Enum1.md) |  | [optional] 
**default** | **object** |  | 
**description** | [**Description**](Description.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.server_variable import ServerVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ServerVariable from a JSON string
server_variable_instance = ServerVariable.from_json(json)
# print the JSON string representation of the object
print ServerVariable.to_json()

# convert the object into a dict
server_variable_dict = server_variable_instance.to_dict()
# create an instance of ServerVariable from a dict
server_variable_form_dict = server_variable.from_dict(server_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


