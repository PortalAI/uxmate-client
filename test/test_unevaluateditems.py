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

from uxmate_client.uxmate_client.unevaluateditems import Unevaluateditems

class TestUnevaluateditems(unittest.TestCase):
    """Unevaluateditems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Unevaluateditems:
        """Test Unevaluateditems
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Unevaluateditems`
        """
        model = Unevaluateditems()
        if include_optional:
            return Unevaluateditems(
                var_schema = None,
                vocabulary = None,
                id = None,
                anchor = None,
                dynamic_anchor = None,
                ref = None,
                dynamic_ref = None,
                defs = None,
                comment = None,
                all_of = None,
                any_of = None,
                one_of = None,
                var_not = None,
                var_if = None,
                then = None,
                var_else = None,
                dependent_schemas = None,
                prefix_items = None,
                items = None,
                contains = None,
                properties = None,
                pattern_properties = None,
                additional_properties = None,
                property_names = None,
                unevaluated_items = None,
                unevaluated_properties = None,
                type = None,
                enum = None,
                const = None,
                multiple_of = None,
                maximum = None,
                exclusive_maximum = None,
                minimum = None,
                exclusive_minimum = None,
                max_length = None,
                min_length = None,
                pattern = None,
                max_items = None,
                min_items = None,
                unique_items = None,
                max_contains = None,
                min_contains = None,
                max_properties = None,
                min_properties = None,
                required = None,
                dependent_required = None,
                format = None,
                content_encoding = None,
                content_media_type = None,
                content_schema = None,
                title = None,
                description = None,
                default = None,
                deprecated = None,
                read_only = None,
                write_only = None,
                examples = None,
                discriminator = None,
                xml = None,
                external_docs = None,
                example = None
            )
        else:
            return Unevaluateditems(
        )
        """

    def testUnevaluateditems(self):
        """Test Unevaluateditems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
