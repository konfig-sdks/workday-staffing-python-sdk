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

from workday_staffing_python_sdk.type.country_related_view7deab99f645f10000cf305c30e260054 import CountryRelatedView7deab99f645f10000cf305c30e260054

Country3b00708994e41000095e4647007012bc = typing.Union[CountryRelatedView7deab99f645f10000cf305c30e260054,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]