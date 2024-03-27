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

from workday_staffing_python_sdk.pydantic.associated_topics_summary_b3a69f47a4991000171aae4c5a810040 import AssociatedTopicsSummaryB3a69f47a4991000171aae4c5a810040
from workday_staffing_python_sdk.pydantic.check_in_attachment_detail_ef244acfe6cf10002ebe92d43a7701d7 import CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7
from workday_staffing_python_sdk.pydantic.creator_b3a69f47a49910001687de28dd71003d import CreatorB3a69f47a49910001687de28dd71003d
from workday_staffing_python_sdk.pydantic.participant_b3a69f47a49910001687de1d4c75003c import ParticipantB3a69f47a49910001687de1d4c75003c

CheckInsSummaryB3a69f47a499100010ce6be72bfe001d = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
