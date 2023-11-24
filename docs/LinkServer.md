# LinkServer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | [**Url**](Url.md) |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**variables** | [**Variables**](Variables.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.link_server import LinkServer

# TODO update the JSON string below
json = "{}"
# create an instance of LinkServer from a JSON string
link_server_instance = LinkServer.from_json(json)
# print the JSON string representation of the object
print LinkServer.to_json()

# convert the object into a dict
link_server_dict = link_server_instance.to_dict()
# create an instance of LinkServer from a dict
link_server_form_dict = link_server.from_dict(link_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


