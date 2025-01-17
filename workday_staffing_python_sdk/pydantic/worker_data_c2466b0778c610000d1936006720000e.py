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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from workday_staffing_python_sdk.pydantic.job_data_for_worker_b8ac205877fd10000ea91719a02a00a2 import JobDataForWorkerB8ac205877fd10000ea91719a02a00a2
from workday_staffing_python_sdk.pydantic.person0ad147648b0a1000237bd486634a001a import Person0ad147648b0a1000237bd486634a001a
from workday_staffing_python_sdk.pydantic.primary_job352c3a97ecd51000353cba144c5b0042 import PrimaryJob352c3a97ecd51000353cba144c5b0042
from workday_staffing_python_sdk.pydantic.worker_type3f78eeedc01d1000138d97d80e5a0000 import WorkerType3f78eeedc01d1000138d97d80e5a0000

WorkerDataC2466b0778c610000d1936006720000e = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
