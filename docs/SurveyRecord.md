# SurveyRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** |  | [optional] 
**survey_id** | **str** |  | 
**business_id** | **str** |  | 
**user_id** | **List[str]** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**chat_history** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**system_message** | **str** |  | [optional] 
**structured_summary** | **object** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 
**survey_ended** | **bool** |  | [optional] [default to False]
**record_state** | [**SurveyRecordState**](SurveyRecordState.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.survey_record import SurveyRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyRecord from a JSON string
survey_record_instance = SurveyRecord.from_json(json)
# print the JSON string representation of the object
print SurveyRecord.to_json()

# convert the object into a dict
survey_record_dict = survey_record_instance.to_dict()
# create an instance of SurveyRecord from a dict
survey_record_form_dict = survey_record.from_dict(survey_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


