# ListSurveysByBusinessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surveys** | [**List[GetSurveyResponse]**](GetSurveyResponse.md) |  | 

## Example

```python
from uxmate_client.models.list_surveys_by_business_response import ListSurveysByBusinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSurveysByBusinessResponse from a JSON string
list_surveys_by_business_response_instance = ListSurveysByBusinessResponse.from_json(json)
# print the JSON string representation of the object
print ListSurveysByBusinessResponse.to_json()

# convert the object into a dict
list_surveys_by_business_response_dict = list_surveys_by_business_response_instance.to_dict()
# create an instance of ListSurveysByBusinessResponse from a dict
list_surveys_by_business_response_form_dict = list_surveys_by_business_response.from_dict(list_surveys_by_business_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


