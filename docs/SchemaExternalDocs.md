# SchemaExternalDocs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Description**](Description.md) |  | [optional] 
**url** | **object** |  | 

## Example

```python
from uxmate_client.uxmate_client.schema_external_docs import SchemaExternalDocs

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaExternalDocs from a JSON string
schema_external_docs_instance = SchemaExternalDocs.from_json(json)
# print the JSON string representation of the object
print SchemaExternalDocs.to_json()

# convert the object into a dict
schema_external_docs_dict = schema_external_docs_instance.to_dict()
# create an instance of SchemaExternalDocs from a dict
schema_external_docs_form_dict = schema_external_docs.from_dict(schema_external_docs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


