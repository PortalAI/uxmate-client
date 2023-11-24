# SendNewMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** |  | 
**survey_id** | **str** |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from uxmate_client.models.send_new_message_request import SendNewMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendNewMessageRequest from a JSON string
send_new_message_request_instance = SendNewMessageRequest.from_json(json)
# print the JSON string representation of the object
print SendNewMessageRequest.to_json()

# convert the object into a dict
send_new_message_request_dict = send_new_message_request_instance.to_dict()
# create an instance of SendNewMessageRequest from a dict
send_new_message_request_form_dict = send_new_message_request.from_dict(send_new_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


