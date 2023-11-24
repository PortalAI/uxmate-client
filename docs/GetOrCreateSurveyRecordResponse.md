# GetOrCreateSurveyRecordResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **str** |  | 
**record_id** | **str** |  | 
**chat_history** | [**ChatHistory**](ChatHistory.md) |  | 
**record_state** | [**SurveyRecordState**](SurveyRecordState.md) |  | 
**description** | **str** |  | 
**survey_name** | **str** |  | 
**assistant_name** | **str** |  | [optional] [default to 'Assistant']

## Example

```python
from uxmate_client.models.get_or_create_survey_record_response import GetOrCreateSurveyRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrCreateSurveyRecordResponse from a JSON string
get_or_create_survey_record_response_instance = GetOrCreateSurveyRecordResponse.from_json(json)
# print the JSON string representation of the object
print GetOrCreateSurveyRecordResponse.to_json()

# convert the object into a dict
get_or_create_survey_record_response_dict = get_or_create_survey_record_response_instance.to_dict()
# create an instance of GetOrCreateSurveyRecordResponse from a dict
get_or_create_survey_record_response_form_dict = get_or_create_survey_record_response.from_dict(get_or_create_survey_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


