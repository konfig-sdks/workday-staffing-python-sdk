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


class CheckInDetail316b5a26cc3c10000ebdb0cb484602e1(
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
                required = {
                    "date",
                }
                
                class properties:
                    description = schemas.StrSchema
                    
                    
                    class associatedTopics(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea']:
                                return AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea'], typing.List['AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'associatedTopics':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea':
                            return super().__getitem__(i)
                    date = schemas.DateSchema
                    
                    
                    class checkInAttachments(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7']:
                                return CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7'], typing.List['CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'checkInAttachments':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7':
                            return super().__getitem__(i)
                    id = schemas.StrSchema
                    __annotations__ = {
                        "description": description,
                        "associatedTopics": associatedTopics,
                        "date": date,
                        "checkInAttachments": checkInAttachments,
                        "id": id,
                    }
            
            date: MetaOapg.properties.date
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["associatedTopics"]) -> MetaOapg.properties.associatedTopics: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["checkInAttachments"]) -> MetaOapg.properties.checkInAttachments: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "associatedTopics", "date", "checkInAttachments", "id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["associatedTopics"]) -> typing.Union[MetaOapg.properties.associatedTopics, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["checkInAttachments"]) -> typing.Union[MetaOapg.properties.checkInAttachments, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "associatedTopics", "date", "checkInAttachments", "id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                date: typing.Union[MetaOapg.properties.date, str, date, ],
                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                associatedTopics: typing.Union[MetaOapg.properties.associatedTopics, list, tuple, schemas.Unset] = schemas.unset,
                checkInAttachments: typing.Union[MetaOapg.properties.checkInAttachments, list, tuple, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    date=date,
                    description=description,
                    associatedTopics=associatedTopics,
                    checkInAttachments=checkInAttachments,
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
    ) -> 'CheckInDetail316b5a26cc3c10000ebdb0cb484602e1':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.associated_check_in_topic_detail316b5a26cc3c100010a01184c23902ea import AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea
from workday_staffing_python_sdk.model.check_in_attachment_detail_ef244acfe6cf10002ebe92d43a7701d7 import CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7
