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

from uxmate_client.uxmate_client.dashboard import Dashboard

class TestDashboard(unittest.TestCase):
    """Dashboard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dashboard:
        """Test Dashboard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dashboard`
        """
        model = Dashboard()
        if include_optional:
            return Dashboard(
                widgets = [
                    uxmate_client.models.widget.Widget(
                        agent = uxmate_client.models.agent.Agent(
                            id = '', 
                            name = '', 
                            assistant_id = '', 
                            assistant_nickname = '', 
                            welcome_message = '', 
                            user_initial_message = '', 
                            icon = '', 
                            visibility_requirements = [
                                ''
                                ], ), 
                        latest_session = uxmate_client.models.session.Session(
                            id = '', 
                            agent_id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            messages = [
                                uxmate_client.models.message.Message(
                                    text = '', 
                                    role = 'user', )
                                ], 
                            status = 'Ready', 
                            routine_id = '', ), )
                    ]
            )
        else:
            return Dashboard(
                widgets = [
                    uxmate_client.models.widget.Widget(
                        agent = uxmate_client.models.agent.Agent(
                            id = '', 
                            name = '', 
                            assistant_id = '', 
                            assistant_nickname = '', 
                            welcome_message = '', 
                            user_initial_message = '', 
                            icon = '', 
                            visibility_requirements = [
                                ''
                                ], ), 
                        latest_session = uxmate_client.models.session.Session(
                            id = '', 
                            agent_id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            messages = [
                                uxmate_client.models.message.Message(
                                    text = '', 
                                    role = 'user', )
                                ], 
                            status = 'Ready', 
                            routine_id = '', ), )
                    ],
        )
        """

    def testDashboard(self):
        """Test Dashboard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
