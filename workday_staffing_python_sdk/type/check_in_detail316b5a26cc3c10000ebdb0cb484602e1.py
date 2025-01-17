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

from workday_staffing_python_sdk.type.associated_check_in_topic_detail316b5a26cc3c100010a01184c23902ea import AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea
from workday_staffing_python_sdk.type.check_in_attachment_detail_ef244acfe6cf10002ebe92d43a7701d7 import CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7

CheckInDetail316b5a26cc3c10000ebdb0cb484602e1 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
