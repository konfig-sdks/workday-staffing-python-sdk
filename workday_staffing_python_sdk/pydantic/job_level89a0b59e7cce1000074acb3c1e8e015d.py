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

from workday_staffing_python_sdk.pydantic.job_level_related_view7deab99f645f10000f06cbbf927a0069 import JobLevelRelatedView7deab99f645f10000f06cbbf927a0069

JobLevel89a0b59e7cce1000074acb3c1e8e015d = typing.Union[JobLevelRelatedView7deab99f645f10000f06cbbf927a0069,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
