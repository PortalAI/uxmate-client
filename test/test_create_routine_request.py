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

from uxmate_client.uxmate_client.create_routine_request import CreateRoutineRequest

class TestCreateRoutineRequest(unittest.TestCase):
    """CreateRoutineRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRoutineRequest:
        """Test CreateRoutineRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRoutineRequest`
        """
        model = CreateRoutineRequest()
        if include_optional:
            return CreateRoutineRequest(
                agent_id = '',
                name = '',
                requirements = '',
                interval = '',
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
            return CreateRoutineRequest(
                agent_id = '',
                name = '',
                requirements = '',
                interval = '',
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

    def testCreateRoutineRequest(self):
        """Test CreateRoutineRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()