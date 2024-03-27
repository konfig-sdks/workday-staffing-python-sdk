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


class WorkerDataC2466b0778c610000d1936006720000e(
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
                    def primaryJob() -> typing.Type['PrimaryJob352c3a97ecd51000353cba144c5b0042']:
                        return PrimaryJob352c3a97ecd51000353cba144c5b0042
                
                    @staticmethod
                    def person() -> typing.Type['Person0ad147648b0a1000237bd486634a001a']:
                        return Person0ad147648b0a1000237bd486634a001a
                    workerId = schemas.StrSchema
                
                    @staticmethod
                    def workerType() -> typing.Type['WorkerType3f78eeedc01d1000138d97d80e5a0000']:
                        return WorkerType3f78eeedc01d1000138d97d80e5a0000
                    
                    
                    class additionalJobs(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['JobDataForWorkerB8ac205877fd10000ea91719a02a00a2']:
                                return JobDataForWorkerB8ac205877fd10000ea91719a02a00a2
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['JobDataForWorkerB8ac205877fd10000ea91719a02a00a2'], typing.List['JobDataForWorkerB8ac205877fd10000ea91719a02a00a2']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additionalJobs':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'JobDataForWorkerB8ac205877fd10000ea91719a02a00a2':
                            return super().__getitem__(i)
                    id = schemas.StrSchema
                    descriptor = schemas.StrSchema
                    __annotations__ = {
                        "primaryJob": primaryJob,
                        "person": person,
                        "workerId": workerId,
                        "workerType": workerType,
                        "additionalJobs": additionalJobs,
                        "id": id,
                        "descriptor": descriptor,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["primaryJob"]) -> 'PrimaryJob352c3a97ecd51000353cba144c5b0042': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["person"]) -> 'Person0ad147648b0a1000237bd486634a001a': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workerId"]) -> MetaOapg.properties.workerId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workerType"]) -> 'WorkerType3f78eeedc01d1000138d97d80e5a0000': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["additionalJobs"]) -> MetaOapg.properties.additionalJobs: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["primaryJob", "person", "workerId", "workerType", "additionalJobs", "id", "descriptor", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["primaryJob"]) -> typing.Union['PrimaryJob352c3a97ecd51000353cba144c5b0042', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["person"]) -> typing.Union['Person0ad147648b0a1000237bd486634a001a', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workerId"]) -> typing.Union[MetaOapg.properties.workerId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workerType"]) -> typing.Union['WorkerType3f78eeedc01d1000138d97d80e5a0000', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["additionalJobs"]) -> typing.Union[MetaOapg.properties.additionalJobs, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["primaryJob", "person", "workerId", "workerType", "additionalJobs", "id", "descriptor", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                primaryJob: typing.Union['PrimaryJob352c3a97ecd51000353cba144c5b0042', schemas.Unset] = schemas.unset,
                person: typing.Union['Person0ad147648b0a1000237bd486634a001a', schemas.Unset] = schemas.unset,
                workerId: typing.Union[MetaOapg.properties.workerId, str, schemas.Unset] = schemas.unset,
                workerType: typing.Union['WorkerType3f78eeedc01d1000138d97d80e5a0000', schemas.Unset] = schemas.unset,
                additionalJobs: typing.Union[MetaOapg.properties.additionalJobs, list, tuple, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    primaryJob=primaryJob,
                    person=person,
                    workerId=workerId,
                    workerType=workerType,
                    additionalJobs=additionalJobs,
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
    ) -> 'WorkerDataC2466b0778c610000d1936006720000e':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.job_data_for_worker_b8ac205877fd10000ea91719a02a00a2 import JobDataForWorkerB8ac205877fd10000ea91719a02a00a2
from workday_staffing_python_sdk.model.person0ad147648b0a1000237bd486634a001a import Person0ad147648b0a1000237bd486634a001a
from workday_staffing_python_sdk.model.primary_job352c3a97ecd51000353cba144c5b0042 import PrimaryJob352c3a97ecd51000353cba144c5b0042
from workday_staffing_python_sdk.model.worker_type3f78eeedc01d1000138d97d80e5a0000 import WorkerType3f78eeedc01d1000138d97d80e5a0000