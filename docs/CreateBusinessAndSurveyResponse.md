# CreateBusinessAndSurveyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | 
**survey_id** | **str** |  | 

## Example

```python
from uxmate_client.uxmate_client.create_business_and_survey_response import CreateBusinessAndSurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBusinessAndSurveyResponse from a JSON string
create_business_and_survey_response_instance = CreateBusinessAndSurveyResponse.from_json(json)
# print the JSON string representation of the object
print CreateBusinessAndSurveyResponse.to_json()

# convert the object into a dict
create_business_and_survey_response_dict = create_business_and_survey_response_instance.to_dict()
# create an instance of CreateBusinessAndSurveyResponse from a dict
create_business_and_survey_response_form_dict = create_business_and_survey_response.from_dict(create_business_and_survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


