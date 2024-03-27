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

from workday_staffing_python_sdk.type.associated_check_in_detail3267c0ba92a0100016ed105476ad03c4 import AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4
from workday_staffing_python_sdk.type.check_in_topic_attachment_detail600ecde4c8421000278d06bfacea01c1 import CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1

CheckInTopicDetail3267c0ba92a010001688d79b032b03b8 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
