# UpdateTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**survey_id** | **str** |  | 
**system_message** | **str** |  | 
**system_message_params** | **List[str]** |  | 
**agent_initial_message** | **str** |  | 
**agent_initial_message_params** | **List[str]** |  | 
**summary_single_prompt** | **str** |  | 
**summary_single_prompt_params** | **List[str]** |  | 
**get_insight_prompt** | **str** |  | 
**get_insight_prompt_params** | **List[str]** |  | 

## Example

```python
from uxmate_client.models.update_template_request import UpdateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateRequest from a JSON string
update_template_request_instance = UpdateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTemplateRequest.to_json()

# convert the object into a dict
update_template_request_dict = update_template_request_instance.to_dict()
# create an instance of UpdateTemplateRequest from a dict
update_template_request_form_dict = update_template_request.from_dict(update_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


