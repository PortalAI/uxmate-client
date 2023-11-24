# Header


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Description**](Description.md) |  | [optional] 
**required** | [**Required**](Required.md) |  | [optional] 
**deprecated** | [**Deprecated**](Deprecated.md) |  | [optional] 
**style** | [**Style**](Style.md) |  | [optional] 
**explode** | [**Explode**](Explode.md) |  | [optional] 
**allow_reserved** | [**Allowreserved**](Allowreserved.md) |  | [optional] 
**var_schema** | [**Schema1**](Schema1.md) |  | [optional] 
**example** | [**Example1**](Example1.md) |  | [optional] 
**examples** | [**Examples**](Examples.md) |  | [optional] 
**content** | [**Content**](Content.md) |  | [optional] 

## Example

```python
from uxmate_client.models.header import Header

# TODO update the JSON string below
json = "{}"
# create an instance of Header from a JSON string
header_instance = Header.from_json(json)
# print the JSON string representation of the object
print Header.to_json()

# convert the object into a dict
header_dict = header_instance.to_dict()
# create an instance of Header from a dict
header_form_dict = header.from_dict(header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


