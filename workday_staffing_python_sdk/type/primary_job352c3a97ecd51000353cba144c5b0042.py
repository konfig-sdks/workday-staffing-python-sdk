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

from workday_staffing_python_sdk.type.job_data_for_worker_b8ac205877fd10000ea91719a02a00a2 import JobDataForWorkerB8ac205877fd10000ea91719a02a00a2

PrimaryJob352c3a97ecd51000353cba144c5b0042 = typing.Union[JobDataForWorkerB8ac205877fd10000ea91719a02a00a2,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
