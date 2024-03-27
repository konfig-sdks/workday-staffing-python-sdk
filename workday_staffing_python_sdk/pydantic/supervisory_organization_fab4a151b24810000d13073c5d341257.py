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

from workday_staffing_python_sdk.pydantic.supervisory_organization_job_view_fab4a151b24810000d29746fb7e21259 import SupervisoryOrganizationJobViewFab4a151b24810000d29746fb7e21259

SupervisoryOrganizationFab4a151b24810000d13073c5d341257 = typing.Union[SupervisoryOrganizationJobViewFab4a151b24810000d29746fb7e21259,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
