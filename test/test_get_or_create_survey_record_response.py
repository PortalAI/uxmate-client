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

from uxmate_client.models.get_or_create_survey_record_response import GetOrCreateSurveyRecordResponse

class TestGetOrCreateSurveyRecordResponse(unittest.TestCase):
    """GetOrCreateSurveyRecordResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOrCreateSurveyRecordResponse:
        """Test GetOrCreateSurveyRecordResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrCreateSurveyRecordResponse`
        """
        model = GetOrCreateSurveyRecordResponse()
        if include_optional:
            return GetOrCreateSurveyRecordResponse(
                survey_id = '',
                record_id = '',
                chat_history = uxmate_client.models.chat_history.ChatHistory(
                    messages = [
                        uxmate_client.models.message.Message(
                            role = 'human', 
                            content = '', )
                        ], ),
                record_state = 'IN_PROGRESS',
                description = '',
                survey_name = '',
                assistant_name = 'Assistant'
            )
        else:
            return GetOrCreateSurveyRecordResponse(
                survey_id = '',
                record_id = '',
                chat_history = uxmate_client.models.chat_history.ChatHistory(
                    messages = [
                        uxmate_client.models.message.Message(
                            role = 'human', 
                            content = '', )
                        ], ),
                record_state = 'IN_PROGRESS',
                description = '',
                survey_name = '',
        )
        """

    def testGetOrCreateSurveyRecordResponse(self):
        """Test GetOrCreateSurveyRecordResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
