# Server


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | [**Url**](Url.md) |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**variables** | [**Variables**](Variables.md) |  | [optional] 

## Example

```python
from uxmate_client.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print Server.to_json()

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_form_dict = server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


