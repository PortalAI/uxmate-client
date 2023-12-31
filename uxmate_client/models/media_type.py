# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from uxmate_client.models.encoding1 import Encoding1
from uxmate_client.models.example1 import Example1
from uxmate_client.models.examples import Examples
from uxmate_client.models.schema1 import Schema1
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MediaType(BaseModel):
    """
    MediaType
    """ # noqa: E501
    var_schema: Optional[Schema1] = Field(default=None, alias="schema")
    example: Optional[Example1] = None
    examples: Optional[Examples] = None
    encoding: Optional[Encoding1] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["schema", "example", "examples", "encoding"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MediaType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of example
        if self.example:
            _dict['example'] = self.example.to_dict()
        # override the default output from pydantic by calling `to_dict()` of examples
        if self.examples:
            _dict['examples'] = self.examples.to_dict()
        # override the default output from pydantic by calling `to_dict()` of encoding
        if self.encoding:
            _dict['encoding'] = self.encoding.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MediaType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": Schema1.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "example": Example1.from_dict(obj.get("example")) if obj.get("example") is not None else None,
            "examples": Examples.from_dict(obj.get("examples")) if obj.get("examples") is not None else None,
            "encoding": Encoding1.from_dict(obj.get("encoding")) if obj.get("encoding") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


