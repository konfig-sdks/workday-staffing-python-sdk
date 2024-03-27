# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import workday_staffing_python_sdk
from workday_staffing_python_sdk.paths.workers_id_check_ins_subresource_i_dtypearchive import patch
from workday_staffing_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWorkersIDCheckInsSubresourceIDtypearchive(ApiTestMixin, unittest.TestCase):
    """
    WorkersIDCheckInsSubresourceIDtypearchive unit test stubs
        Partially updates an existing Check-In to archived or un-archived.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()