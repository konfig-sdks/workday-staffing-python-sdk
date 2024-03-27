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

from workday_staffing_python_sdk.pydantic.person86093b8a932f10001499f38c72410130 import Person86093b8a932f10001499f38c72410130

Comments86093b8a932f10001499f356ff83012e = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
