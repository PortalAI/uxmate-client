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
from uxmate_client.models.description import Description
from uxmate_client.models.link_server import LinkServer
from uxmate_client.models.operationid import Operationid
from uxmate_client.models.operationref import Operationref
from uxmate_client.models.parameters import Parameters
from uxmate_client.models.requestbody import Requestbody
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Link(BaseModel):
    """
    Link
    """ # noqa: E501
    operation_ref: Optional[Operationref] = Field(default=None, alias="operationRef")
    operation_id: Optional[Operationid] = Field(default=None, alias="operationId")
    parameters: Optional[Parameters] = None
    request_body: Optional[Requestbody] = Field(default=None, alias="requestBody")
    description: Optional[Description] = None
    server: Optional[LinkServer] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["operationRef", "operationId", "parameters", "requestBody", "description", "server"]

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
        """Create an instance of Link from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of operation_ref
        if self.operation_ref:
            _dict['operationRef'] = self.operation_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_id
        if self.operation_id:
            _dict['operationId'] = self.operation_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of request_body
        if self.request_body:
            _dict['requestBody'] = self.request_body.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Link from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operationRef": Operationref.from_dict(obj.get("operationRef")) if obj.get("operationRef") is not None else None,
            "operationId": Operationid.from_dict(obj.get("operationId")) if obj.get("operationId") is not None else None,
            "parameters": Parameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "requestBody": Requestbody.from_dict(obj.get("requestBody")) if obj.get("requestBody") is not None else None,
            "description": Description.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "server": LinkServer.from_dict(obj.get("server")) if obj.get("server") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


