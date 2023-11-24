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

from uxmate_client.uxmate_client.header import Header

class TestHeader(unittest.TestCase):
    """Header unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Header:
        """Test Header
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Header`
        """
        model = Header()
        if include_optional:
            return Header(
                description = None,
                required = None,
                deprecated = None,
                style = None,
                explode = None,
                allow_reserved = None,
                var_schema = None,
                example = None,
                examples = None,
                content = None
            )
        else:
            return Header(
        )
        """

    def testHeader(self):
        """Test Header"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()