# GetSurveyRecordSummaryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** |  | 
**chat_summary** | **str** |  | 

## Example

```python
from uxmate_client.uxmate_client.get_survey_record_summary_response import GetSurveyRecordSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSurveyRecordSummaryResponse from a JSON string
get_survey_record_summary_response_instance = GetSurveyRecordSummaryResponse.from_json(json)
# print the JSON string representation of the object
print GetSurveyRecordSummaryResponse.to_json()

# convert the object into a dict
get_survey_record_summary_response_dict = get_survey_record_summary_response_instance.to_dict()
# create an instance of GetSurveyRecordSummaryResponse from a dict
get_survey_record_summary_response_form_dict = get_survey_record_summary_response.from_dict(get_survey_record_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


