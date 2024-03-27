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

from workday_staffing_python_sdk.type.organization_assignment_changes_business_unit_data5aabf8e28cb310002520b2a2b31d0365 import OrganizationAssignmentChangesBusinessUnitData5aabf8e28cb310002520b2a2b31d0365

class RequiredOrganizationAssignmentChangesGetBusinessUnitResponse(TypedDict):
    pass

class OptionalOrganizationAssignmentChangesGetBusinessUnitResponse(TypedDict, total=False):
    data: typing.List[OrganizationAssignmentChangesBusinessUnitData5aabf8e28cb310002520b2a2b31d0365]

    total: int

class OrganizationAssignmentChangesGetBusinessUnitResponse(RequiredOrganizationAssignmentChangesGetBusinessUnitResponse, OptionalOrganizationAssignmentChangesGetBusinessUnitResponse):
    pass