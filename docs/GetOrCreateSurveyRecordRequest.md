# GetOrCreateSurveyRecordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **str** |  | 
**record_id** | **str** |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.get_or_create_survey_record_request import GetOrCreateSurveyRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrCreateSurveyRecordRequest from a JSON string
get_or_create_survey_record_request_instance = GetOrCreateSurveyRecordRequest.from_json(json)
# print the JSON string representation of the object
print GetOrCreateSurveyRecordRequest.to_json()

# convert the object into a dict
get_or_create_survey_record_request_dict = get_or_create_survey_record_request_instance.to_dict()
# create an instance of GetOrCreateSurveyRecordRequest from a dict
get_or_create_survey_record_request_form_dict = get_or_create_survey_record_request.from_dict(get_or_create_survey_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


