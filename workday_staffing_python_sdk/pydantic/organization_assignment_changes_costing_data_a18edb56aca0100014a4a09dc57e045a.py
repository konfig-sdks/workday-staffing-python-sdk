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

from workday_staffing_python_sdk.pydantic.fund_a18edb56aca0100014a4a0b27352045c import FundA18edb56aca0100014a4a0b27352045c
from workday_staffing_python_sdk.pydantic.gift_a18edb56aca0100014a4a0a9f876045b import GiftA18edb56aca0100014a4a0a9f876045b
from workday_staffing_python_sdk.pydantic.grant_a18edb56aca0100014a4a0bcf25c045e import GrantA18edb56aca0100014a4a0bcf25c045e
from workday_staffing_python_sdk.pydantic.program_a18edb56aca0100014a4a0b7ddf7045d import ProgramA18edb56aca0100014a4a0b7ddf7045d

OrganizationAssignmentChangesCostingDataA18edb56aca0100014a4a09dc57e045a = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]