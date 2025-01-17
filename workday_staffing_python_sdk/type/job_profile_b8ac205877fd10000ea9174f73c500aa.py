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

from workday_staffing_python_sdk.type.job_profile_job_view_fab4a151b24810000d511d61ee641262 import JobProfileJobViewFab4a151b24810000d511d61ee641262

JobProfileB8ac205877fd10000ea9174f73c500aa = typing.Union[JobProfileJobViewFab4a151b24810000d511d61ee641262,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
