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

from uxmate_client.uxmate_client.get_business_list_response import GetBusinessListResponse

class TestGetBusinessListResponse(unittest.TestCase):
    """GetBusinessListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBusinessListResponse:
        """Test GetBusinessListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBusinessListResponse`
        """
        model = GetBusinessListResponse()
        if include_optional:
            return GetBusinessListResponse(
                businesses = [
                    uxmate_client.models.get_business_response.GetBusinessResponse(
                        business_id = '', 
                        business_name = '', 
                        business_description = '', )
                    ]
            )
        else:
            return GetBusinessListResponse(
                businesses = [
                    uxmate_client.models.get_business_response.GetBusinessResponse(
                        business_id = '', 
                        business_name = '', 
                        business_description = '', )
                    ],
        )
        """

    def testGetBusinessListResponse(self):
        """Test GetBusinessListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()