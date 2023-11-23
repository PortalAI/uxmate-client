# CreateTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **str** |  | 
**system_message** | **str** |  | [optional] 
**system_message_params** | [**AnyOf**](AnyOf.md) |  | [optional] 
**agent_initial_message** | **str** |  | [optional] 
**agent_initial_message_params** | **List[str]** |  | [optional] 
**summary_single_prompt** | **str** |  | [optional] 
**summary_single_prompt_params** | [**AnyOf**](AnyOf.md) |  | [optional] 
**get_insight_prompt** | **str** |  | [optional] 
**get_insight_prompt_params** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_template_request import CreateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequest from a JSON string
create_template_request_instance = CreateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print CreateTemplateRequest.to_json()

# convert the object into a dict
create_template_request_dict = create_template_request_instance.to_dict()
# create an instance of CreateTemplateRequest from a dict
create_template_request_form_dict = create_template_request.from_dict(create_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


