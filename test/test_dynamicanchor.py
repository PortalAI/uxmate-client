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

from openapi_client.models.dynamicanchor import Dynamicanchor

class TestDynamicanchor(unittest.TestCase):
    """Dynamicanchor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dynamicanchor:
        """Test Dynamicanchor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dynamicanchor`
        """
        model = Dynamicanchor()
        if include_optional:
            return Dynamicanchor(
            )
        else:
            return Dynamicanchor(
        )
        """

    def testDynamicanchor(self):
        """Test Dynamicanchor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
