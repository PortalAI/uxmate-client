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

from uxmate_client.uxmate_client.xml import XML

class TestXML(unittest.TestCase):
    """XML unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> XML:
        """Test XML
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `XML`
        """
        model = XML()
        if include_optional:
            return XML(
                name = None,
                namespace = None,
                prefix = None,
                attribute = None,
                wrapped = None
            )
        else:
            return XML(
        )
        """

    def testXML(self):
        """Test XML"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()