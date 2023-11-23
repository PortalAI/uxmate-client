# UpdateSurveyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**survey_id** | **str** |  | 
**survey_name** | **str** |  | 
**survey_description** | **str** |  | 
**initial_message** | **str** |  | 

## Example

```python
from openapi_client.models.update_survey_response import UpdateSurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSurveyResponse from a JSON string
update_survey_response_instance = UpdateSurveyResponse.from_json(json)
# print the JSON string representation of the object
print UpdateSurveyResponse.to_json()

# convert the object into a dict
update_survey_response_dict = update_survey_response_instance.to_dict()
# create an instance of UpdateSurveyResponse from a dict
update_survey_response_form_dict = update_survey_response.from_dict(update_survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


