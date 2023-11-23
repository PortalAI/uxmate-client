# CreateSurveyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | [optional] 
**business_name** | **str** |  | [optional] [default to '']
**business_description** | **str** |  | [optional] [default to '']
**survey_name** | **str** |  | 
**survey_description** | **str** |  | 
**quota** | **int** |  | [optional] [default to 1000]
**initial_message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_survey_request import CreateSurveyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSurveyRequest from a JSON string
create_survey_request_instance = CreateSurveyRequest.from_json(json)
# print the JSON string representation of the object
print CreateSurveyRequest.to_json()

# convert the object into a dict
create_survey_request_dict = create_survey_request_instance.to_dict()
# create an instance of CreateSurveyRequest from a dict
create_survey_request_form_dict = create_survey_request.from_dict(create_survey_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


