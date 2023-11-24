# SchemaXml


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
from uxmate_client.uxmate_client.schema_xml import SchemaXml

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaXml from a JSON string
schema_xml_instance = SchemaXml.from_json(json)
# print the JSON string representation of the object
print SchemaXml.to_json()

# convert the object into a dict
schema_xml_dict = schema_xml_instance.to_dict()
# create an instance of SchemaXml from a dict
schema_xml_form_dict = schema_xml.from_dict(schema_xml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


