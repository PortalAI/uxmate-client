# XML


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | [optional] 
**namespace** | [**Namespace**](Namespace.md) |  | [optional] 
**prefix** | [**Prefix**](Prefix.md) |  | [optional] 
**attribute** | [**Attribute**](Attribute.md) |  | [optional] 
**wrapped** | [**Wrapped**](Wrapped.md) |  | [optional] 

## Example

```python
from openapi_client.models.xml import XML

# TODO update the JSON string below
json = "{}"
# create an instance of XML from a JSON string
xml_instance = XML.from_json(json)
# print the JSON string representation of the object
print XML.to_json()

# convert the object into a dict
xml_dict = xml_instance.to_dict()
# create an instance of XML from a dict
xml_form_dict = xml.from_dict(xml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


