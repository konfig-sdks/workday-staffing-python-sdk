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


class CheckInTopicDetail3267c0ba92a010001688d79b032b03b8(
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
                    sharedNotes = schemas.StrSchema
                    
                    
                    class associatedCheckIns(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4']:
                                return AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4'], typing.List['AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'associatedCheckIns':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4':
                            return super().__getitem__(i)
                    privateNotes = schemas.StrSchema
                    name = schemas.StrSchema
                    
                    
                    class checkInTopicAttachments(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1']:
                                return CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1'], typing.List['CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'checkInTopicAttachments':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1':
                            return super().__getitem__(i)
                    id = schemas.StrSchema
                    __annotations__ = {
                        "sharedNotes": sharedNotes,
                        "associatedCheckIns": associatedCheckIns,
                        "privateNotes": privateNotes,
                        "name": name,
                        "checkInTopicAttachments": checkInTopicAttachments,
                        "id": id,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sharedNotes"]) -> MetaOapg.properties.sharedNotes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["associatedCheckIns"]) -> MetaOapg.properties.associatedCheckIns: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["privateNotes"]) -> MetaOapg.properties.privateNotes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["checkInTopicAttachments"]) -> MetaOapg.properties.checkInTopicAttachments: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["sharedNotes", "associatedCheckIns", "privateNotes", "name", "checkInTopicAttachments", "id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sharedNotes"]) -> typing.Union[MetaOapg.properties.sharedNotes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["associatedCheckIns"]) -> typing.Union[MetaOapg.properties.associatedCheckIns, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["privateNotes"]) -> typing.Union[MetaOapg.properties.privateNotes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["checkInTopicAttachments"]) -> typing.Union[MetaOapg.properties.checkInTopicAttachments, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sharedNotes", "associatedCheckIns", "privateNotes", "name", "checkInTopicAttachments", "id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                sharedNotes: typing.Union[MetaOapg.properties.sharedNotes, str, schemas.Unset] = schemas.unset,
                associatedCheckIns: typing.Union[MetaOapg.properties.associatedCheckIns, list, tuple, schemas.Unset] = schemas.unset,
                privateNotes: typing.Union[MetaOapg.properties.privateNotes, str, schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                checkInTopicAttachments: typing.Union[MetaOapg.properties.checkInTopicAttachments, list, tuple, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    sharedNotes=sharedNotes,
                    associatedCheckIns=associatedCheckIns,
                    privateNotes=privateNotes,
                    name=name,
                    checkInTopicAttachments=checkInTopicAttachments,
                    id=id,
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
    ) -> 'CheckInTopicDetail3267c0ba92a010001688d79b032b03b8':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.associated_check_in_detail3267c0ba92a0100016ed105476ad03c4 import AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4
from workday_staffing_python_sdk.model.check_in_topic_attachment_detail600ecde4c8421000278d06bfacea01c1 import CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1
