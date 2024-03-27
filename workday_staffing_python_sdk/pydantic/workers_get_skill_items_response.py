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

from workday_staffing_python_sdk.pydantic.skill_item_display_definition4b4b7d34b4a21000301eaf52086700d8 import SkillItemDisplayDefinition4b4b7d34b4a21000301eaf52086700d8

class WorkersGetSkillItemsResponse(BaseModel):
    data: typing.Optional[typing.List[SkillItemDisplayDefinition4b4b7d34b4a21000301eaf52086700d8]] = Field(None, alias='data')

    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
