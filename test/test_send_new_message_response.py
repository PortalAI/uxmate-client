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

from uxmate_client.models.send_new_message_response import SendNewMessageResponse

class TestSendNewMessageResponse(unittest.TestCase):
    """SendNewMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendNewMessageResponse:
        """Test SendNewMessageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendNewMessageResponse`
        """
        model = SendNewMessageResponse()
        if include_optional:
            return SendNewMessageResponse(
                messages = uxmate_client.models.chat_history.ChatHistory(
                    messages = [
                        uxmate_client.models.message.Message(
                            role = 'human', 
                            content = '', )
                        ], ),
                record_state = 'IN_PROGRESS'
            )
        else:
            return SendNewMessageResponse(
                messages = uxmate_client.models.chat_history.ChatHistory(
                    messages = [
                        uxmate_client.models.message.Message(
                            role = 'human', 
                            content = '', )
                        ], ),
                record_state = 'IN_PROGRESS',
        )
        """

    def testSendNewMessageResponse(self):
        """Test SendNewMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
