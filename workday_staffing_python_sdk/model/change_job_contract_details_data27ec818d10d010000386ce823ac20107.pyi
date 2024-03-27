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


class ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    assignmentDetails = schemas.StrSchema
                    contractEndDate = schemas.DateSchema
                    contractPayRate = schemas.DictSchema
                
                    @staticmethod
                    def currency() -> typing.Type['Currency2d0ca2cb2448100009c54386a8570e07']:
                        return Currency2d0ca2cb2448100009c54386a8570e07
                
                    @staticmethod
                    def frequency() -> typing.Type['Frequency2d0ca2cb2448100009c5436d5d670e06']:
                        return Frequency2d0ca2cb2448100009c5436d5d670e06
                
                    @staticmethod
                    def purchaseOrder() -> typing.Type['PurchaseOrder2d0ca2cb2448100009c5433bcff60e05']:
                        return PurchaseOrder2d0ca2cb2448100009c5433bcff60e05
                    __annotations__ = {
                        "assignmentDetails": assignmentDetails,
                        "contractEndDate": contractEndDate,
                        "contractPayRate": contractPayRate,
                        "currency": currency,
                        "frequency": frequency,
                        "purchaseOrder": purchaseOrder,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["assignmentDetails"]) -> MetaOapg.properties.assignmentDetails: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contractEndDate"]) -> MetaOapg.properties.contractEndDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contractPayRate"]) -> MetaOapg.properties.contractPayRate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'Currency2d0ca2cb2448100009c54386a8570e07': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> 'Frequency2d0ca2cb2448100009c5436d5d670e06': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["purchaseOrder"]) -> 'PurchaseOrder2d0ca2cb2448100009c5433bcff60e05': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["assignmentDetails", "contractEndDate", "contractPayRate", "currency", "frequency", "purchaseOrder", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["assignmentDetails"]) -> typing.Union[MetaOapg.properties.assignmentDetails, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contractEndDate"]) -> typing.Union[MetaOapg.properties.contractEndDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contractPayRate"]) -> typing.Union[MetaOapg.properties.contractPayRate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union['Currency2d0ca2cb2448100009c54386a8570e07', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union['Frequency2d0ca2cb2448100009c5436d5d670e06', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["purchaseOrder"]) -> typing.Union['PurchaseOrder2d0ca2cb2448100009c5433bcff60e05', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assignmentDetails", "contractEndDate", "contractPayRate", "currency", "frequency", "purchaseOrder", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                assignmentDetails: typing.Union[MetaOapg.properties.assignmentDetails, str, schemas.Unset] = schemas.unset,
                contractEndDate: typing.Union[MetaOapg.properties.contractEndDate, str, date, schemas.Unset] = schemas.unset,
                contractPayRate: typing.Union[MetaOapg.properties.contractPayRate, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                currency: typing.Union['Currency2d0ca2cb2448100009c54386a8570e07', schemas.Unset] = schemas.unset,
                frequency: typing.Union['Frequency2d0ca2cb2448100009c5436d5d670e06', schemas.Unset] = schemas.unset,
                purchaseOrder: typing.Union['PurchaseOrder2d0ca2cb2448100009c5433bcff60e05', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    assignmentDetails=assignmentDetails,
                    contractEndDate=contractEndDate,
                    contractPayRate=contractPayRate,
                    currency=currency,
                    frequency=frequency,
                    purchaseOrder=purchaseOrder,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.currency2d0ca2cb2448100009c54386a8570e07 import Currency2d0ca2cb2448100009c54386a8570e07
from workday_staffing_python_sdk.model.frequency2d0ca2cb2448100009c5436d5d670e06 import Frequency2d0ca2cb2448100009c5436d5d670e06
from workday_staffing_python_sdk.model.purchase_order2d0ca2cb2448100009c5433bcff60e05 import PurchaseOrder2d0ca2cb2448100009c5433bcff60e05
