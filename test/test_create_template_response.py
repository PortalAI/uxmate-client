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

from openapi_client.models.create_template_response import CreateTemplateResponse

class TestCreateTemplateResponse(unittest.TestCase):
    """CreateTemplateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTemplateResponse:
        """Test CreateTemplateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTemplateResponse`
        """
        model = CreateTemplateResponse()
        if include_optional:
            return CreateTemplateResponse(
                template_id = '',
                survey_id = '',
                system_message = '',
                system_message_params = [
                    ''
                    ],
                agent_initial_message = '',
                agent_initial_message_params = [
                    ''
                    ],
                summary_single_prompt = '',
                summary_single_prompt_params = [
                    ''
                    ],
                get_insight_prompt = '',
                get_insight_prompt_params = [
                    ''
                    ]
            )
        else:
            return CreateTemplateResponse(
                template_id = '',
                survey_id = '',
                system_message = '',
                system_message_params = [
                    ''
                    ],
                agent_initial_message = '',
                agent_initial_message_params = [
                    ''
                    ],
                summary_single_prompt = '',
                summary_single_prompt_params = [
                    ''
                    ],
                get_insight_prompt = '',
                get_insight_prompt_params = [
                    ''
                    ],
        )
        """

    def testCreateTemplateResponse(self):
        """Test CreateTemplateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
