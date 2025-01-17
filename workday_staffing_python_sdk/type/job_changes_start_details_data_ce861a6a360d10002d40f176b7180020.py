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

from workday_staffing_python_sdk.type.job35b8f199c29410002508ffd7ad6101f3 import Job35b8f199c29410002508ffd7ad6101f3
from workday_staffing_python_sdk.type.location6da81665c26510001fc6b1d42fae5f7b import Location6da81665c26510001fc6b1d42fae5f7b
from workday_staffing_python_sdk.type.reason6da81665c26510001f34d0a154765e9b import Reason6da81665c26510001f34d0a154765e9b
from workday_staffing_python_sdk.type.supervisory_organization_e3267ea37e6f100032c00c34a99e74d8 import SupervisoryOrganizationE3267ea37e6f100032c00c34a99e74d8
from workday_staffing_python_sdk.type.template2b1b95dfe4af100009f30dc769a31686 import Template2b1b95dfe4af100009f30dc769a31686
from workday_staffing_python_sdk.type.worker271bbd673582100010110b9f9a6d99e1 import Worker271bbd673582100010110b9f9a6d99e1

JobChangesStartDetailsDataCe861a6a360d10002d40f176b7180020 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
