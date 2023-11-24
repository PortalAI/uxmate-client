# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from uxmate_client.models.update_survey_request import UpdateSurveyRequest

class TestUpdateSurveyRequest(unittest.TestCase):
    """UpdateSurveyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSurveyRequest:
        """Test UpdateSurveyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSurveyRequest`
        """
        model = UpdateSurveyRequest()
        if include_optional:
            return UpdateSurveyRequest(
                business_id = '',
                survey_id = '',
                survey_name = '',
                system_prompt = '',
                survey_description = '',
                initial_message = ''
            )
        else:
            return UpdateSurveyRequest(
                business_id = '',
                survey_id = '',
                survey_name = '',
                system_prompt = '',
                survey_description = '',
                initial_message = '',
        )
        """

    def testUpdateSurveyRequest(self):
        """Test UpdateSurveyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
