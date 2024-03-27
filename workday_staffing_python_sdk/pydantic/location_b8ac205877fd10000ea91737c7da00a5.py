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

from workday_staffing_python_sdk.pydantic.location_data_job_view6d3eb084b4c410002b5fa13f0c9d0056 import LocationDataJobView6d3eb084b4c410002b5fa13f0c9d0056

LocationB8ac205877fd10000ea91737c7da00a5 = typing.Union[LocationDataJobView6d3eb084b4c410002b5fa13f0c9d0056,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
