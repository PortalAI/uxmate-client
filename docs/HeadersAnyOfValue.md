# HeadersAnyOfValue


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
**ref** | **object** |  | 

## Example

```python
from uxmate_client.models.headers_any_of_value import HeadersAnyOfValue

# TODO update the JSON string below
json = "{}"
# create an instance of HeadersAnyOfValue from a JSON string
headers_any_of_value_instance = HeadersAnyOfValue.from_json(json)
# print the JSON string representation of the object
print HeadersAnyOfValue.to_json()

# convert the object into a dict
headers_any_of_value_dict = headers_any_of_value_instance.to_dict()
# create an instance of HeadersAnyOfValue from a dict
headers_any_of_value_form_dict = headers_any_of_value.from_dict(headers_any_of_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


