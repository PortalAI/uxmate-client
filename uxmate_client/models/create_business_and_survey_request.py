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
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateBusinessAndSurveyRequest(BaseModel):
    """
    CreateBusinessAndSurveyRequest
    """ # noqa: E501
    survey_name: StrictStr
    survey_description: StrictStr
    business_name: StrictStr
    business_description: StrictStr
    system_prompt: StrictStr
    initial_message: StrictStr
    quota: Optional[StrictInt] = 1000
    __properties: ClassVar[List[str]] = ["survey_name", "survey_description", "business_name", "business_description", "system_prompt", "initial_message", "quota"]

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
        """Create an instance of CreateBusinessAndSurveyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateBusinessAndSurveyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "survey_name": obj.get("survey_name"),
            "survey_description": obj.get("survey_description"),
            "business_name": obj.get("business_name"),
            "business_description": obj.get("business_description"),
            "system_prompt": obj.get("system_prompt"),
            "initial_message": obj.get("initial_message"),
            "quota": obj.get("quota") if obj.get("quota") is not None else 1000
        })
        return _obj


