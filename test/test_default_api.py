# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from uxmate_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_chat_with_bot_chat_post(self) -> None:
        """Test case for chat_with_bot_chat_post

        Chat With Bot
        """
        pass

    def test_create_business_and_survey_business_and_survey_post(self) -> None:
        """Test case for create_business_and_survey_business_and_survey_post

        Create Business And Survey
        """
        pass

    def test_create_business_business_post(self) -> None:
        """Test case for create_business_business_post

        Create Business
        """
        pass

    def test_create_survey_survey_post(self) -> None:
        """Test case for create_survey_survey_post

        Create Survey
        """
        pass

    def test_create_template_template_post(self) -> None:
        """Test case for create_template_template_post

        Create Template
        """
        pass

    def test_delete_business(self) -> None:
        """Test case for delete_business

        Delete Business
        """
        pass

    def test_delete_survey(self) -> None:
        """Test case for delete_survey

        Delete Survey
        """
        pass

    def test_delete_survey_record(self) -> None:
        """Test case for delete_survey_record

        Delete Survey Record
        """
        pass

    def test_get_business_business_business_id_get(self) -> None:
        """Test case for get_business_business_business_id_get

        Get Business
        """
        pass

    def test_get_businesses_business_get(self) -> None:
        """Test case for get_businesses_business_get

        Get Businesses
        """
        pass

    def test_get_chat_history_chat_history_record_id_get(self) -> None:
        """Test case for get_chat_history_chat_history_record_id_get

        Get Chat History
        """
        pass

    def test_get_create_survey_record_survey_record_post(self) -> None:
        """Test case for get_create_survey_record_survey_record_post

        Get Create Survey Record
        """
        pass

    def test_get_survey_insight_survey_survey_id_insight_get(self) -> None:
        """Test case for get_survey_insight_survey_survey_id_insight_get

        Get Survey Insight
        """
        pass

    def test_get_survey_record_survey_record_record_id_get(self) -> None:
        """Test case for get_survey_record_survey_record_record_id_get

        Get Survey Record
        """
        pass

    def test_get_survey_summary_survey_record_record_id_summary_get(self) -> None:
        """Test case for get_survey_summary_survey_record_record_id_summary_get

        Get Survey Summary
        """
        pass

    def test_get_survey_survey_survey_id_get(self) -> None:
        """Test case for get_survey_survey_survey_id_get

        Get Survey
        """
        pass

    def test_get_survey_xlsx_survey_survey_id_report_xlsx_get(self) -> None:
        """Test case for get_survey_xlsx_survey_survey_id_report_xlsx_get

        Get Survey Xlsx
        """
        pass

    def test_get_surveys(self) -> None:
        """Test case for get_surveys

        Get Surveys
        """
        pass

    def test_get_surveys_list_by_business_id_business_business_id_survey_get(self) -> None:
        """Test case for get_surveys_list_by_business_id_business_business_id_survey_get

        Get Surveys List By Business Id
        """
        pass

    def test_get_template_by_survey_id_survey_survey_id_template_get(self) -> None:
        """Test case for get_template_by_survey_id_survey_survey_id_template_get

        Get Template By Survey Id
        """
        pass

    def test_get_template_template_template_id_get(self) -> None:
        """Test case for get_template_template_template_id_get

        Get Template
        """
        pass

    def test_health_check_health_check_get(self) -> None:
        """Test case for health_check_health_check_get

        Health Check
        """
        pass

    def test_init_survey_insight_survey_survey_id_insight_new_put(self) -> None:
        """Test case for init_survey_insight_survey_survey_id_insight_new_put

        Init Survey Insight
        """
        pass

    def test_init_survey_summary_survey_record_record_id_summary_new_put(self) -> None:
        """Test case for init_survey_summary_survey_record_record_id_summary_new_put

        Init Survey Summary
        """
        pass

    def test_list_survey_records_survey_survey_id_records_get(self) -> None:
        """Test case for list_survey_records_survey_survey_id_records_get

        List Survey Records
        """
        pass

    def test_root_get(self) -> None:
        """Test case for root_get

        Root
        """
        pass

    def test_update_business_business_put(self) -> None:
        """Test case for update_business_business_put

        Update Business
        """
        pass

    def test_update_survey(self) -> None:
        """Test case for update_survey

        Update Survey
        """
        pass

    def test_update_template_template_put(self) -> None:
        """Test case for update_template_template_put

        Update Template
        """
        pass


if __name__ == '__main__':
    unittest.main()
