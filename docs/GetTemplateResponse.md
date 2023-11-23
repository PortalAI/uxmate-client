# GetTemplateResponse


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
from openapi_client.models.get_template_response import GetTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplateResponse from a JSON string
get_template_response_instance = GetTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetTemplateResponse.to_json()

# convert the object into a dict
get_template_response_dict = get_template_response_instance.to_dict()
# create an instance of GetTemplateResponse from a dict
get_template_response_form_dict = get_template_response.from_dict(get_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


