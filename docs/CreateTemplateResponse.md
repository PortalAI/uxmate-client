# CreateTemplateResponse


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
from openapi_client.models.create_template_response import CreateTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateResponse from a JSON string
create_template_response_instance = CreateTemplateResponse.from_json(json)
# print the JSON string representation of the object
print CreateTemplateResponse.to_json()

# convert the object into a dict
create_template_response_dict = create_template_response_instance.to_dict()
# create an instance of CreateTemplateResponse from a dict
create_template_response_form_dict = create_template_response.from_dict(create_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


