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

from workday_staffing_python_sdk.type.change_job_business_title3db8095ffa18100013a5f96969ca0102 import ChangeJobBusinessTitle3db8095ffa18100013a5f96969ca0102

class RequiredJobChangesGetBusinessTitleResponse(TypedDict):
    pass

class OptionalJobChangesGetBusinessTitleResponse(TypedDict, total=False):
    data: typing.List[ChangeJobBusinessTitle3db8095ffa18100013a5f96969ca0102]

    total: int

class JobChangesGetBusinessTitleResponse(RequiredJobChangesGetBusinessTitleResponse, OptionalJobChangesGetBusinessTitleResponse):
    pass
