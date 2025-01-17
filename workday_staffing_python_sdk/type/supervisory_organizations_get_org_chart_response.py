# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from workday_staffing_python_sdk.type.org_chart_view643e3a12629710000554e0338e670044 import OrgChartView643e3a12629710000554e0338e670044

class RequiredSupervisoryOrganizationsGetOrgChartResponse(TypedDict):
    pass

class OptionalSupervisoryOrganizationsGetOrgChartResponse(TypedDict, total=False):
    data: typing.List[OrgChartView643e3a12629710000554e0338e670044]

    total: int

class SupervisoryOrganizationsGetOrgChartResponse(RequiredSupervisoryOrganizationsGetOrgChartResponse, OptionalSupervisoryOrganizationsGetOrgChartResponse):
    pass
