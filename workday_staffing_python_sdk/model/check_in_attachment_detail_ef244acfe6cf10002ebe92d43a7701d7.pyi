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


class CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7(
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
                    
                    
                    class fileName(
                        schemas.StrSchema
                    ):
                        pass
                
                    @staticmethod
                    def contentType() -> typing.Type['ContentTypeEf244acfe6cf10002ebe92e7001601d8']:
                        return ContentTypeEf244acfe6cf10002ebe92e7001601d8
                    comment = schemas.StrSchema
                    fileLength = schemas.IntSchema
                    id = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    __annotations__ = {
                        "fileName": fileName,
                        "contentType": contentType,
                        "comment": comment,
                        "fileLength": fileLength,
                        "id": id,
                        "descriptor": descriptor,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contentType"]) -> 'ContentTypeEf244acfe6cf10002ebe92e7001601d8': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileLength"]) -> MetaOapg.properties.fileLength: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileName", "contentType", "comment", "fileLength", "id", "descriptor", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contentType"]) -> typing.Union['ContentTypeEf244acfe6cf10002ebe92e7001601d8', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileLength"]) -> typing.Union[MetaOapg.properties.fileLength, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileName", "contentType", "comment", "fileLength", "id", "descriptor", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
                contentType: typing.Union['ContentTypeEf244acfe6cf10002ebe92e7001601d8', schemas.Unset] = schemas.unset,
                comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
                fileLength: typing.Union[MetaOapg.properties.fileLength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    fileName=fileName,
                    contentType=contentType,
                    comment=comment,
                    fileLength=fileLength,
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
    ) -> 'CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.content_type_ef244acfe6cf10002ebe92e7001601d8 import ContentTypeEf244acfe6cf10002ebe92e7001601d8