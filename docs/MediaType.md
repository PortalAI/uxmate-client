# MediaType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**Schema1**](Schema1.md) |  | [optional] 
**example** | [**Example1**](Example1.md) |  | [optional] 
**examples** | [**Examples**](Examples.md) |  | [optional] 
**encoding** | [**Encoding1**](Encoding1.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.media_type import MediaType

# TODO update the JSON string below
json = "{}"
# create an instance of MediaType from a JSON string
media_type_instance = MediaType.from_json(json)
# print the JSON string representation of the object
print MediaType.to_json()

# convert the object into a dict
media_type_dict = media_type_instance.to_dict()
# create an instance of MediaType from a dict
media_type_form_dict = media_type.from_dict(media_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


