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

from uxmate_client.uxmate_client.create_survey_request import CreateSurveyRequest

class TestCreateSurveyRequest(unittest.TestCase):
    """CreateSurveyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSurveyRequest:
        """Test CreateSurveyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSurveyRequest`
        """
        model = CreateSurveyRequest()
        if include_optional:
            return CreateSurveyRequest(
                business_id = '',
                business_name = '',
                business_description = '',
                survey_name = '',
                survey_description = '',
                quota = 56,
                initial_message = ''
            )
        else:
            return CreateSurveyRequest(
                survey_name = '',
                survey_description = '',
        )
        """

    def testCreateSurveyRequest(self):
        """Test CreateSurveyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()