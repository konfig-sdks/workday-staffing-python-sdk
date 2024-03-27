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

from workday_staffing_python_sdk.type.job_family_view51ed1475e9e6100005d10fcedc5a000a import JobFamilyView51ed1475e9e6100005d10fcedc5a000a

class RequiredJobFamiliesListResponse(TypedDict):
    pass

class OptionalJobFamiliesListResponse(TypedDict, total=False):
    data: typing.List[JobFamilyView51ed1475e9e6100005d10fcedc5a000a]

    total: int

class JobFamiliesListResponse(RequiredJobFamiliesListResponse, OptionalJobFamiliesListResponse):
    pass
