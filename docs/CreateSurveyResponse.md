# CreateSurveyResponse


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
from uxmate_client.uxmate_client.create_survey_response import CreateSurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSurveyResponse from a JSON string
create_survey_response_instance = CreateSurveyResponse.from_json(json)
# print the JSON string representation of the object
print CreateSurveyResponse.to_json()

# convert the object into a dict
create_survey_response_dict = create_survey_response_instance.to_dict()
# create an instance of CreateSurveyResponse from a dict
create_survey_response_form_dict = create_survey_response.from_dict(create_survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


