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


class SupervisoryOrganizationViewA02c2e1916fa100009e137235f1f0018(
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
                    name = schemas.StrSchema
                    
                    
                    class managers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ManagerWorkerViewA02c2e1916fa10000cbb84be81ce0027']:
                                return ManagerWorkerViewA02c2e1916fa10000cbb84be81ce0027
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ManagerWorkerViewA02c2e1916fa10000cbb84be81ce0027'], typing.List['ManagerWorkerViewA02c2e1916fa10000cbb84be81ce0027']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'managers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ManagerWorkerViewA02c2e1916fa10000cbb84be81ce0027':
                            return super().__getitem__(i)
                    code = schemas.StrSchema
                    inactive = schemas.BoolSchema
                    id = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    __annotations__ = {
                        "name": name,
                        "managers": managers,
                        "code": code,
                        "inactive": inactive,
                        "id": id,
                        "descriptor": descriptor,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["managers"]) -> MetaOapg.properties.managers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inactive"]) -> MetaOapg.properties.inactive: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "managers", "code", "inactive", "id", "descriptor", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["managers"]) -> typing.Union[MetaOapg.properties.managers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inactive"]) -> typing.Union[MetaOapg.properties.inactive, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "managers", "code", "inactive", "id", "descriptor", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                managers: typing.Union[MetaOapg.properties.managers, list, tuple, schemas.Unset] = schemas.unset,
                code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
                inactive: typing.Union[MetaOapg.properties.inactive, bool, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    name=name,
                    managers=managers,
                    code=code,
                    inactive=inactive,
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
    ) -> 'SupervisoryOrganizationViewA02c2e1916fa100009e137235f1f0018':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.manager_worker_view_a02c2e1916fa10000cbb84be81ce0027 import ManagerWorkerViewA02c2e1916fa10000cbb84be81ce0027
