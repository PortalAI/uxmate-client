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

class GetSurveyResponse(BaseModel):
    """
    GetSurveyResponse
    """ # noqa: E501
    business_id: StrictStr
    survey_id: StrictStr
    survey_name: StrictStr
    survey_description: StrictStr
    system_prompt: StrictStr
    initial_message: StrictStr
    insight: StrictStr
    survey_records_count: Optional[StrictInt] = None
    chat_link: StrictStr
    __properties: ClassVar[List[str]] = ["business_id", "survey_id", "survey_name", "survey_description", "system_prompt", "initial_message", "insight", "survey_records_count", "chat_link"]

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
        """Create an instance of GetSurveyResponse from a JSON string"""
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
        # set to None if survey_records_count (nullable) is None
        # and model_fields_set contains the field
        if self.survey_records_count is None and "survey_records_count" in self.model_fields_set:
            _dict['survey_records_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetSurveyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "business_id": obj.get("business_id"),
            "survey_id": obj.get("survey_id"),
            "survey_name": obj.get("survey_name"),
            "survey_description": obj.get("survey_description"),
            "system_prompt": obj.get("system_prompt"),
            "initial_message": obj.get("initial_message"),
            "insight": obj.get("insight"),
            "survey_records_count": obj.get("survey_records_count"),
            "chat_link": obj.get("chat_link")
        })
        return _obj

