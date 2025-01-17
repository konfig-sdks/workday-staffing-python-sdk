# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from workday_staffing_python_sdk import schemas  # noqa: F401


class FACETSMODELREFERENCE(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['FACETSMODELREFERENCEItem']:
            return FACETSMODELREFERENCEItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['FACETSMODELREFERENCEItem'], typing.List['FACETSMODELREFERENCEItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FACETSMODELREFERENCE':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'FACETSMODELREFERENCEItem':
        return super().__getitem__(i)

from workday_staffing_python_sdk.model.facetsmodelreference_item import FACETSMODELREFERENCEItem
