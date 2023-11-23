# GetChatHistoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_history** | [**ChatHistory**](ChatHistory.md) |  | 

## Example

```python
from openapi_client.models.get_chat_history_response import GetChatHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatHistoryResponse from a JSON string
get_chat_history_response_instance = GetChatHistoryResponse.from_json(json)
# print the JSON string representation of the object
print GetChatHistoryResponse.to_json()

# convert the object into a dict
get_chat_history_response_dict = get_chat_history_response_instance.to_dict()
# create an instance of GetChatHistoryResponse from a dict
get_chat_history_response_form_dict = get_chat_history_response.from_dict(get_chat_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


