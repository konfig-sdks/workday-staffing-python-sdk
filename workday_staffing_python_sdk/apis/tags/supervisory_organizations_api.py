# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

from workday_staffing_python_sdk.paths.supervisory_organizations.get import GetById
from workday_staffing_python_sdk.paths.supervisory_organizations_id.get import GetInstance
from workday_staffing_python_sdk.paths.supervisory_organizations_id_members_subresource_id.get import GetMember
from workday_staffing_python_sdk.paths.supervisory_organizations_id_members.get import GetMembers
from workday_staffing_python_sdk.paths.supervisory_organizations_id_org_chart.get import GetOrgChart
from workday_staffing_python_sdk.paths.supervisory_organizations_id_org_chart_subresource_id.get import GetOrgChart0
from workday_staffing_python_sdk.apis.tags.supervisory_organizations_api_raw import SupervisoryOrganizationsApiRaw


class SupervisoryOrganizationsApi(
    GetById,
    GetInstance,
    GetMember,
    GetMembers,
    GetOrgChart,
    GetOrgChart0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SupervisoryOrganizationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SupervisoryOrganizationsApiRaw(api_client)
