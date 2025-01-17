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


class ChangeJobPositionDataDfc4e58f7308100018bd1c459f435221(
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
                    createPosition = schemas.BoolSchema
                    availableForOverlap = schemas.BoolSchema
                
                    @staticmethod
                    def position() -> typing.Type['PositionDfc4e58f730810001ad60369c23452d1']:
                        return PositionDfc4e58f730810001ad60369c23452d1
                    closePosition = schemas.BoolSchema
                
                    @staticmethod
                    def jobRequisition() -> typing.Type['JobRequisitionDfc4e58f730810001ad60325d9bc52cf']:
                        return JobRequisitionDfc4e58f730810001ad60325d9bc52cf
                    id = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    __annotations__ = {
                        "createPosition": createPosition,
                        "availableForOverlap": availableForOverlap,
                        "position": position,
                        "closePosition": closePosition,
                        "jobRequisition": jobRequisition,
                        "id": id,
                        "descriptor": descriptor,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["createPosition"]) -> MetaOapg.properties.createPosition: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["availableForOverlap"]) -> MetaOapg.properties.availableForOverlap: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["position"]) -> 'PositionDfc4e58f730810001ad60369c23452d1': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["closePosition"]) -> MetaOapg.properties.closePosition: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobRequisition"]) -> 'JobRequisitionDfc4e58f730810001ad60325d9bc52cf': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["createPosition", "availableForOverlap", "position", "closePosition", "jobRequisition", "id", "descriptor", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["createPosition"]) -> typing.Union[MetaOapg.properties.createPosition, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["availableForOverlap"]) -> typing.Union[MetaOapg.properties.availableForOverlap, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union['PositionDfc4e58f730810001ad60369c23452d1', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["closePosition"]) -> typing.Union[MetaOapg.properties.closePosition, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobRequisition"]) -> typing.Union['JobRequisitionDfc4e58f730810001ad60325d9bc52cf', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["createPosition", "availableForOverlap", "position", "closePosition", "jobRequisition", "id", "descriptor", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                createPosition: typing.Union[MetaOapg.properties.createPosition, bool, schemas.Unset] = schemas.unset,
                availableForOverlap: typing.Union[MetaOapg.properties.availableForOverlap, bool, schemas.Unset] = schemas.unset,
                position: typing.Union['PositionDfc4e58f730810001ad60369c23452d1', schemas.Unset] = schemas.unset,
                closePosition: typing.Union[MetaOapg.properties.closePosition, bool, schemas.Unset] = schemas.unset,
                jobRequisition: typing.Union['JobRequisitionDfc4e58f730810001ad60325d9bc52cf', schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    createPosition=createPosition,
                    availableForOverlap=availableForOverlap,
                    position=position,
                    closePosition=closePosition,
                    jobRequisition=jobRequisition,
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
    ) -> 'ChangeJobPositionDataDfc4e58f7308100018bd1c459f435221':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.job_requisition_dfc4e58f730810001ad60325d9bc52cf import JobRequisitionDfc4e58f730810001ad60325d9bc52cf
from workday_staffing_python_sdk.model.position_dfc4e58f730810001ad60369c23452d1 import PositionDfc4e58f730810001ad60369c23452d1
