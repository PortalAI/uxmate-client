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

from uxmate_client.uxmate_client.routine import Routine

class TestRoutine(unittest.TestCase):
    """Routine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Routine:
        """Test Routine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Routine`
        """
        model = Routine()
        if include_optional:
            return Routine(
                id = '',
                agent_id = '',
                name = '',
                requirements = '',
                interval = '',
                trend = uxmate_client.models.trend.Trend(
                    description = '', 
                    status = 'POSITIVE', ),
                data_source = uxmate_client.models.data_source.DataSource(
                    endpoints = [
                        uxmate_client.models.endpoint_data_source.EndpointDataSource(
                            url = '', 
                            method = '', 
                            description = '', )
                        ], 
                    sql_tables = [
                        uxmate_client.models.sql_tables_data_source.SqlTablesDataSource(
                            connection_string = '', 
                            table_name = '', )
                        ], 
                    google_tables = [
                        uxmate_client.models.google_table_data_source.GoogleTableDataSource(
                            spreadsheet_id = '', 
                            sheet_name = '', )
                        ], 
                    local_files = [
                        uxmate_client.models.local_file_data_source.LocalFileDataSource(
                            path = '', )
                        ], )
            )
        else:
            return Routine(
                id = '',
                agent_id = '',
                name = '',
                requirements = '',
                interval = '',
                trend = uxmate_client.models.trend.Trend(
                    description = '', 
                    status = 'POSITIVE', ),
                data_source = uxmate_client.models.data_source.DataSource(
                    endpoints = [
                        uxmate_client.models.endpoint_data_source.EndpointDataSource(
                            url = '', 
                            method = '', 
                            description = '', )
                        ], 
                    sql_tables = [
                        uxmate_client.models.sql_tables_data_source.SqlTablesDataSource(
                            connection_string = '', 
                            table_name = '', )
                        ], 
                    google_tables = [
                        uxmate_client.models.google_table_data_source.GoogleTableDataSource(
                            spreadsheet_id = '', 
                            sheet_name = '', )
                        ], 
                    local_files = [
                        uxmate_client.models.local_file_data_source.LocalFileDataSource(
                            path = '', )
                        ], ),
        )
        """

    def testRoutine(self):
        """Test Routine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
