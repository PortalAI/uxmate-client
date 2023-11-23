# ChatHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) |  | 

## Example

```python
from openapi_client.models.chat_history import ChatHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ChatHistory from a JSON string
chat_history_instance = ChatHistory.from_json(json)
# print the JSON string representation of the object
print ChatHistory.to_json()

# convert the object into a dict
chat_history_dict = chat_history_instance.to_dict()
# create an instance of ChatHistory from a dict
chat_history_form_dict = chat_history.from_dict(chat_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


