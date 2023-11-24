# ExamplesAnyOfValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**Summary**](Summary.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 
**external_value** | [**Externalvalue**](Externalvalue.md) |  | [optional] 
**ref** | **object** |  | 

## Example

```python
from uxmate_client.uxmate_client.examples_any_of_value import ExamplesAnyOfValue

# TODO update the JSON string below
json = "{}"
# create an instance of ExamplesAnyOfValue from a JSON string
examples_any_of_value_instance = ExamplesAnyOfValue.from_json(json)
# print the JSON string representation of the object
print ExamplesAnyOfValue.to_json()

# convert the object into a dict
examples_any_of_value_dict = examples_any_of_value_instance.to_dict()
# create an instance of ExamplesAnyOfValue from a dict
examples_any_of_value_form_dict = examples_any_of_value.from_dict(examples_any_of_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


