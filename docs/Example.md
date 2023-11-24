# Example


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**Summary**](Summary.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 
**external_value** | [**Externalvalue**](Externalvalue.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.example import Example

# TODO update the JSON string below
json = "{}"
# create an instance of Example from a JSON string
example_instance = Example.from_json(json)
# print the JSON string representation of the object
print Example.to_json()

# convert the object into a dict
example_dict = example_instance.to_dict()
# create an instance of Example from a dict
example_form_dict = example.from_dict(example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


