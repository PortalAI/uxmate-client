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

from openapi_client.models.get_chat_history_response import GetChatHistoryResponse

class TestGetChatHistoryResponse(unittest.TestCase):
    """GetChatHistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetChatHistoryResponse:
        """Test GetChatHistoryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetChatHistoryResponse`
        """
        model = GetChatHistoryResponse()
        if include_optional:
            return GetChatHistoryResponse(
                chat_history = openapi_client.models.chat_history.ChatHistory(
                    messages = [
                        openapi_client.models.message.Message(
                            role = 'human', 
                            content = '', )
                        ], )
            )
        else:
            return GetChatHistoryResponse(
                chat_history = openapi_client.models.chat_history.ChatHistory(
                    messages = [
                        openapi_client.models.message.Message(
                            role = 'human', 
                            content = '', )
                        ], ),
        )
        """

    def testGetChatHistoryResponse(self):
        """Test GetChatHistoryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
