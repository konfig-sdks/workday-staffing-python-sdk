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

from workday_staffing_python_sdk.type.change_job_contract_details_data27ec818d10d010000386ce823ac20107 import ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107

class RequiredJobChangesGetContractOptionsResponse(TypedDict):
    pass

class OptionalJobChangesGetContractOptionsResponse(TypedDict, total=False):
    data: typing.List[ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107]

    total: int

class JobChangesGetContractOptionsResponse(RequiredJobChangesGetContractOptionsResponse, OptionalJobChangesGetContractOptionsResponse):
    pass
