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

from workday_staffing_python_sdk.type.display_explicit_skill_representation_d6ca778018011000182fa5be1ae901a8 import DisplayExplicitSkillRepresentationD6ca778018011000182fa5be1ae901a8
from workday_staffing_python_sdk.type.skill_item98f198f5056b100019631445471d225f import SkillItem98f198f5056b100019631445471d225f
from workday_staffing_python_sdk.type.skill_item_source_add_representation_c5fabc4ca81610000d5d15309ac90122 import SkillItemSourceAddRepresentationC5fabc4ca81610000d5d15309ac90122

CreateSkillUsageRepresentation98f198f5056b1000196313ffe9a0225e = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
