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


class EventState54e611eca2c910000fbc4579181c0111(
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
                
                    @staticmethod
                    def businessProcessParameters() -> typing.Type['BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261']:
                        return BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261
                
                    @staticmethod
                    def status() -> typing.Type['Status54e611eca2c910000fbc4599be0b0112']:
                        return Status54e611eca2c910000fbc4599be0b0112
                    validation = schemas.StrSchema
                    id = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    __annotations__ = {
                        "businessProcessParameters": businessProcessParameters,
                        "status": status,
                        "validation": validation,
                        "id": id,
                        "descriptor": descriptor,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["businessProcessParameters"]) -> 'BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'Status54e611eca2c910000fbc4599be0b0112': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["validation"]) -> MetaOapg.properties.validation: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["businessProcessParameters", "status", "validation", "id", "descriptor", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["businessProcessParameters"]) -> typing.Union['BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['Status54e611eca2c910000fbc4599be0b0112', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["validation"]) -> typing.Union[MetaOapg.properties.validation, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["businessProcessParameters", "status", "validation", "id", "descriptor", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                businessProcessParameters: typing.Union['BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261', schemas.Unset] = schemas.unset,
                status: typing.Union['Status54e611eca2c910000fbc4599be0b0112', schemas.Unset] = schemas.unset,
                validation: typing.Union[MetaOapg.properties.validation, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    businessProcessParameters=businessProcessParameters,
                    status=status,
                    validation=validation,
                    id=id,
                    descriptor=descriptor,
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
    ) -> 'EventState54e611eca2c910000fbc4579181c0111':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.business_process_parameters5afc0b4b5a4610002aaebb8180cd2261 import BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261
from workday_staffing_python_sdk.model.status54e611eca2c910000fbc4599be0b0112 import Status54e611eca2c910000fbc4599be0b0112