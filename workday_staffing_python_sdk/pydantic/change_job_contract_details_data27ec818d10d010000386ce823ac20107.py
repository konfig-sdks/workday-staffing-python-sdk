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

from workday_staffing_python_sdk.pydantic.currency2d0ca2cb2448100009c54386a8570e07 import Currency2d0ca2cb2448100009c54386a8570e07
from workday_staffing_python_sdk.pydantic.frequency2d0ca2cb2448100009c5436d5d670e06 import Frequency2d0ca2cb2448100009c5436d5d670e06
from workday_staffing_python_sdk.pydantic.purchase_order2d0ca2cb2448100009c5433bcff60e05 import PurchaseOrder2d0ca2cb2448100009c5433bcff60e05

ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107 = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
