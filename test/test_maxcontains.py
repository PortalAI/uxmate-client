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

from uxmate_client.uxmate_client.maxcontains import Maxcontains

class TestMaxcontains(unittest.TestCase):
    """Maxcontains unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Maxcontains:
        """Test Maxcontains
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Maxcontains`
        """
        model = Maxcontains()
        if include_optional:
            return Maxcontains(
            )
        else:
            return Maxcontains(
        )
        """

    def testMaxcontains(self):
        """Test Maxcontains"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
