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

from workday_staffing_python_sdk.pydantic.pay_rate_type_related_view3b00708994e410000c52776049ba12c3 import PayRateTypeRelatedView3b00708994e410000c52776049ba12c3

PayRateType3b00708994e410000c3d01aea96012c1 = typing.Union[PayRateTypeRelatedView3b00708994e410000c52776049ba12c3,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]