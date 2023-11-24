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

from uxmate_client.models.survey_record import SurveyRecord

class TestSurveyRecord(unittest.TestCase):
    """SurveyRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SurveyRecord:
        """Test SurveyRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SurveyRecord`
        """
        model = SurveyRecord()
        if include_optional:
            return SurveyRecord(
                record_id = '',
                survey_id = '',
                business_id = '',
                user_id = [
                    ''
                    ],
                customer_id = '',
                chat_history = '',
                summary = '',
                system_message = '',
                structured_summary = uxmate_client.models.structured_summary.structured_summary(),
                created_at = '',
                updated_at = '',
                survey_ended = True,
                record_state = 'IN_PROGRESS'
            )
        else:
            return SurveyRecord(
                survey_id = '',
                business_id = '',
                created_at = '',
        )
        """

    def testSurveyRecord(self):
        """Test SurveyRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
