# SchemaDiscriminator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **object** |  | 
**mapping** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_discriminator import SchemaDiscriminator

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaDiscriminator from a JSON string
schema_discriminator_instance = SchemaDiscriminator.from_json(json)
# print the JSON string representation of the object
print SchemaDiscriminator.to_json()

# convert the object into a dict
schema_discriminator_dict = schema_discriminator_instance.to_dict()
# create an instance of SchemaDiscriminator from a dict
schema_discriminator_form_dict = schema_discriminator.from_dict(schema_discriminator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


