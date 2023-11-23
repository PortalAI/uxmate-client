# SendNewMessageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**ChatHistory**](ChatHistory.md) |  | 
**record_state** | [**SurveyRecordState**](SurveyRecordState.md) |  | 

## Example

```python
from openapi_client.models.send_new_message_response import SendNewMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendNewMessageResponse from a JSON string
send_new_message_response_instance = SendNewMessageResponse.from_json(json)
# print the JSON string representation of the object
print SendNewMessageResponse.to_json()

# convert the object into a dict
send_new_message_response_dict = send_new_message_response_instance.to_dict()
# create an instance of SendNewMessageResponse from a dict
send_new_message_response_form_dict = send_new_message_response.from_dict(send_new_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


