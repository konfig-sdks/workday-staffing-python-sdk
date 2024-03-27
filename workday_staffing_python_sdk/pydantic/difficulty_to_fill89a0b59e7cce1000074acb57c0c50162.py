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

from workday_staffing_python_sdk.pydantic.difficulty_to_fill_related_view3b00708994e41000032f4de84695004c import DifficultyToFillRelatedView3b00708994e41000032f4de84695004c

DifficultyToFill89a0b59e7cce1000074acb57c0c50162 = typing.Union[DifficultyToFillRelatedView3b00708994e41000032f4de84695004c,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
