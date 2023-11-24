# ListSurveysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surveys** | [**List[GetSurveyResponse]**](GetSurveyResponse.md) |  | 

## Example

```python
from uxmate_client.uxmate_client.list_surveys_response import ListSurveysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSurveysResponse from a JSON string
list_surveys_response_instance = ListSurveysResponse.from_json(json)
# print the JSON string representation of the object
print ListSurveysResponse.to_json()

# convert the object into a dict
list_surveys_response_dict = list_surveys_response_instance.to_dict()
# create an instance of ListSurveysResponse from a dict
list_surveys_response_form_dict = list_surveys_response.from_dict(list_surveys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


