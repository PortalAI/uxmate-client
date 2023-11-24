# GetSurveyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**survey_id** | **str** |  | 
**survey_name** | **str** |  | 
**survey_description** | **str** |  | 
**system_prompt** | **str** |  | 
**initial_message** | **str** |  | 
**insight** | **str** |  | 
**survey_records_count** | **int** |  | [optional] 
**chat_link** | **str** |  | 

## Example

```python
from uxmate_client.uxmate_client.get_survey_response import GetSurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSurveyResponse from a JSON string
get_survey_response_instance = GetSurveyResponse.from_json(json)
# print the JSON string representation of the object
print GetSurveyResponse.to_json()

# convert the object into a dict
get_survey_response_dict = get_survey_response_instance.to_dict()
# create an instance of GetSurveyResponse from a dict
get_survey_response_form_dict = get_survey_response.from_dict(get_survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


