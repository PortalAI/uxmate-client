# Unevaluatedproperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**vocabulary** | [**Vocabulary**](Vocabulary.md) |  | [optional] 
**id** | [**Id**](Id.md) |  | [optional] 
**anchor** | [**Anchor**](Anchor.md) |  | [optional] 
**dynamic_anchor** | [**Dynamicanchor**](Dynamicanchor.md) |  | [optional] 
**ref** | [**Ref**](Ref.md) |  | [optional] 
**dynamic_ref** | [**Dynamicref**](Dynamicref.md) |  | [optional] 
**defs** | [**Defs**](Defs.md) |  | [optional] 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**all_of** | [**Allof**](Allof.md) |  | [optional] 
**any_of** | [**Anyof**](Anyof.md) |  | [optional] 
**one_of** | [**Oneof**](Oneof.md) |  | [optional] 
**var_not** | [**ModelNot**](ModelNot.md) |  | [optional] 
**var_if** | [**ModelIf**](ModelIf.md) |  | [optional] 
**then** | [**Then**](Then.md) |  | [optional] 
**var_else** | [**ModelElse**](ModelElse.md) |  | [optional] 
**dependent_schemas** | [**Dependentschemas**](Dependentschemas.md) |  | [optional] 
**prefix_items** | [**Prefixitems**](Prefixitems.md) |  | [optional] 
**items** | [**Items**](Items.md) |  | [optional] 
**contains** | [**Contains**](Contains.md) |  | [optional] 
**properties** | [**Properties**](Properties.md) |  | [optional] 
**pattern_properties** | [**Patternproperties**](Patternproperties.md) |  | [optional] 
**additional_properties** | [**Additionalproperties**](Additionalproperties.md) |  | [optional] 
**property_names** | [**Propertynames**](Propertynames.md) |  | [optional] 
**unevaluated_items** | [**Unevaluateditems**](Unevaluateditems.md) |  | [optional] 
**unevaluated_properties** | [**Unevaluatedproperties**](Unevaluatedproperties.md) |  | [optional] 
**type** | [**Type**](Type.md) |  | [optional] 
**enum** | [**Enum**](Enum.md) |  | [optional] 
**const** | [**Const**](Const.md) |  | [optional] 
**multiple_of** | [**Multipleof**](Multipleof.md) |  | [optional] 
**maximum** | [**Maximum**](Maximum.md) |  | [optional] 
**exclusive_maximum** | [**Exclusivemaximum**](Exclusivemaximum.md) |  | [optional] 
**minimum** | [**Minimum**](Minimum.md) |  | [optional] 
**exclusive_minimum** | [**Exclusiveminimum**](Exclusiveminimum.md) |  | [optional] 
**max_length** | [**Maxlength**](Maxlength.md) |  | [optional] 
**min_length** | [**Minlength**](Minlength.md) |  | [optional] 
**pattern** | [**Pattern**](Pattern.md) |  | [optional] 
**max_items** | [**Maxitems**](Maxitems.md) |  | [optional] 
**min_items** | [**Minitems**](Minitems.md) |  | [optional] 
**unique_items** | [**Uniqueitems**](Uniqueitems.md) |  | [optional] 
**max_contains** | [**Maxcontains**](Maxcontains.md) |  | [optional] 
**min_contains** | [**Mincontains**](Mincontains.md) |  | [optional] 
**max_properties** | [**Maxproperties**](Maxproperties.md) |  | [optional] 
**min_properties** | [**Minproperties**](Minproperties.md) |  | [optional] 
**required** | [**Required1**](Required1.md) |  | [optional] 
**dependent_required** | [**Dependentrequired**](Dependentrequired.md) |  | [optional] 
**format** | [**Format**](Format.md) |  | [optional] 
**content_encoding** | [**Contentencoding**](Contentencoding.md) |  | [optional] 
**content_media_type** | [**Contentmediatype**](Contentmediatype.md) |  | [optional] 
**content_schema** | [**Contentschema**](Contentschema.md) |  | [optional] 
**title** | [**Title**](Title.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**default** | [**Default**](Default.md) |  | [optional] 
**deprecated** | [**Deprecated**](Deprecated.md) |  | [optional] 
**read_only** | [**Readonly**](Readonly.md) |  | [optional] 
**write_only** | [**Writeonly**](Writeonly.md) |  | [optional] 
**examples** | [**Examples1**](Examples1.md) |  | [optional] 
**discriminator** | [**SchemaDiscriminator**](SchemaDiscriminator.md) |  | [optional] 
**xml** | [**SchemaXml**](SchemaXml.md) |  | [optional] 
**external_docs** | [**SchemaExternalDocs**](SchemaExternalDocs.md) |  | [optional] 
**example** | [**Example1**](Example1.md) |  | [optional] 

## Example

```python
from uxmate_client.uxmate_client.unevaluatedproperties import Unevaluatedproperties

# TODO update the JSON string below
json = "{}"
# create an instance of Unevaluatedproperties from a JSON string
unevaluatedproperties_instance = Unevaluatedproperties.from_json(json)
# print the JSON string representation of the object
print Unevaluatedproperties.to_json()

# convert the object into a dict
unevaluatedproperties_dict = unevaluatedproperties_instance.to_dict()
# create an instance of Unevaluatedproperties from a dict
unevaluatedproperties_form_dict = unevaluatedproperties.from_dict(unevaluatedproperties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


