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

from workday_staffing_python_sdk.pydantic.category43b30ba735b8100011ee4781a9d50146 import Category43b30ba735b8100011ee4781a9d50146
from workday_staffing_python_sdk.pydantic.content_type43b30ba735b8100011ee47993f11014a import ContentType43b30ba735b8100011ee47993f11014a
from workday_staffing_python_sdk.pydantic.uploaded_by_b32ff437243510000e22e06470370160 import UploadedByB32ff437243510000e22e06470370160

EventAttachmentsForToolbar43b30ba735b8100011ee4767246d0143 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]