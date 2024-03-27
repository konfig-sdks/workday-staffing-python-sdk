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
from workday_staffing_python_sdk.paths.job_changes_id_job_classification_subresource_id import get
from workday_staffing_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestJobChangesIDJobClassificationSubresourceID(ApiTestMixin, unittest.TestCase):
    """
    JobChangesIDJobClassificationSubresourceID unit test stubs
        Retrieves a job classification for the specified job change ID.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
