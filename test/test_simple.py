# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from workday_staffing_python_sdk import WorkdayStaffing

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        workdaystaffing = WorkdayStaffing(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(workdaystaffing)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
