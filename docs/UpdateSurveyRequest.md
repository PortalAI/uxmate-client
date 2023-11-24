# UpdateSurveyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**survey_id** | **str** |  | 
**survey_name** | **str** |  | 
**system_prompt** | **str** |  | 
**survey_description** | **str** |  | 
**initial_message** | **str** |  | 

## Example

```python
from uxmate_client.uxmate_client.update_survey_request import UpdateSurveyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSurveyRequest from a JSON string
update_survey_request_instance = UpdateSurveyRequest.from_json(json)
# print the JSON string representation of the object
print UpdateSurveyRequest.to_json()

# convert the object into a dict
update_survey_request_dict = update_survey_request_instance.to_dict()
# create an instance of UpdateSurveyRequest from a dict
update_survey_request_form_dict = update_survey_request.from_dict(update_survey_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


