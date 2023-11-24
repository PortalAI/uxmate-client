# ListSurveyRecordsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[SurveyRecord]**](SurveyRecord.md) |  | 

## Example

```python
from uxmate_client.uxmate_client.list_survey_records_response import ListSurveyRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSurveyRecordsResponse from a JSON string
list_survey_records_response_instance = ListSurveyRecordsResponse.from_json(json)
# print the JSON string representation of the object
print ListSurveyRecordsResponse.to_json()

# convert the object into a dict
list_survey_records_response_dict = list_survey_records_response_instance.to_dict()
# create an instance of ListSurveyRecordsResponse from a dict
list_survey_records_response_form_dict = list_survey_records_response.from_dict(list_survey_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


