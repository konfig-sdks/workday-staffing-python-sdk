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

from workday_staffing_python_sdk.pydantic.change_job_move_team_data544fdf5c01da1000238ad82d26d90146 import ChangeJobMoveTeamData544fdf5c01da1000238ad82d26d90146

class JobChangesGetMoveTeamOptionResponse(BaseModel):
    data: typing.Optional[typing.List[ChangeJobMoveTeamData544fdf5c01da1000238ad82d26d90146]] = Field(None, alias='data')

    total: typing.Optional[int] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
