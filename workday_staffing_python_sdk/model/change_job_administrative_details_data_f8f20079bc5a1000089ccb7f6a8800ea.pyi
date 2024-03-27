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


class ChangeJobAdministrativeDetailsDataF8f20079bc5a1000089ccb7f6a8800ea(
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
                    def payRateType() -> typing.Type['PayRateTypeD25283821c01100016756a14eb650000']:
                        return PayRateTypeD25283821c01100016756a14eb650000
                
                    @staticmethod
                    def workersCompensationCodeOverride() -> typing.Type['WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f']:
                        return WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f
                    fte = schemas.IntSchema
                    notifyBy = schemas.DateSchema
                    
                    
                    class companyInsiderTypes(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137']:
                                return ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137'], typing.List['ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'companyInsiderTypes':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137':
                            return super().__getitem__(i)
                    firstDayOfWork = schemas.DateSchema
                    defaultWeeklyHours = schemas.IntSchema
                
                    @staticmethod
                    def positionWorkerType() -> typing.Type['PositionWorkerType05d4c45042b610001030ee47f2c90118']:
                        return PositionWorkerType05d4c45042b610001030ee47f2c90118
                    workingFte = schemas.IntSchema
                    specifyWorkingFte = schemas.BoolSchema
                
                    @staticmethod
                    def timeType() -> typing.Type['TimeType05d4c45042b610000bb540b7458e0108']:
                        return TimeType05d4c45042b610000bb540b7458e0108
                    specifyPaidFte = schemas.BoolSchema
                    paidFte = schemas.IntSchema
                
                    @staticmethod
                    def workStudy() -> typing.Type['WorkStudy05d4c45042b610000ba2f83c70f30101']:
                        return WorkStudy05d4c45042b610000ba2f83c70f30101
                
                    @staticmethod
                    def assignmentType() -> typing.Type['AssignmentType23929e1f68ca10000d6940d6bde56963']:
                        return AssignmentType23929e1f68ca10000d6940d6bde56963
                    endEmploymentDate = schemas.DateSchema
                    expectedAssignmentEndDate = schemas.DateSchema
                    __annotations__ = {
                        "payRateType": payRateType,
                        "workersCompensationCodeOverride": workersCompensationCodeOverride,
                        "fte": fte,
                        "notifyBy": notifyBy,
                        "companyInsiderTypes": companyInsiderTypes,
                        "firstDayOfWork": firstDayOfWork,
                        "defaultWeeklyHours": defaultWeeklyHours,
                        "positionWorkerType": positionWorkerType,
                        "workingFte": workingFte,
                        "specifyWorkingFte": specifyWorkingFte,
                        "timeType": timeType,
                        "specifyPaidFte": specifyPaidFte,
                        "paidFte": paidFte,
                        "workStudy": workStudy,
                        "assignmentType": assignmentType,
                        "endEmploymentDate": endEmploymentDate,
                        "expectedAssignmentEndDate": expectedAssignmentEndDate,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["payRateType"]) -> 'PayRateTypeD25283821c01100016756a14eb650000': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workersCompensationCodeOverride"]) -> 'WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fte"]) -> MetaOapg.properties.fte: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["notifyBy"]) -> MetaOapg.properties.notifyBy: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["companyInsiderTypes"]) -> MetaOapg.properties.companyInsiderTypes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["firstDayOfWork"]) -> MetaOapg.properties.firstDayOfWork: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["defaultWeeklyHours"]) -> MetaOapg.properties.defaultWeeklyHours: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["positionWorkerType"]) -> 'PositionWorkerType05d4c45042b610001030ee47f2c90118': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workingFte"]) -> MetaOapg.properties.workingFte: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["specifyWorkingFte"]) -> MetaOapg.properties.specifyWorkingFte: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["timeType"]) -> 'TimeType05d4c45042b610000bb540b7458e0108': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["specifyPaidFte"]) -> MetaOapg.properties.specifyPaidFte: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["paidFte"]) -> MetaOapg.properties.paidFte: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workStudy"]) -> 'WorkStudy05d4c45042b610000ba2f83c70f30101': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["assignmentType"]) -> 'AssignmentType23929e1f68ca10000d6940d6bde56963': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["endEmploymentDate"]) -> MetaOapg.properties.endEmploymentDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["expectedAssignmentEndDate"]) -> MetaOapg.properties.expectedAssignmentEndDate: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["payRateType", "workersCompensationCodeOverride", "fte", "notifyBy", "companyInsiderTypes", "firstDayOfWork", "defaultWeeklyHours", "positionWorkerType", "workingFte", "specifyWorkingFte", "timeType", "specifyPaidFte", "paidFte", "workStudy", "assignmentType", "endEmploymentDate", "expectedAssignmentEndDate", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["payRateType"]) -> typing.Union['PayRateTypeD25283821c01100016756a14eb650000', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workersCompensationCodeOverride"]) -> typing.Union['WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fte"]) -> typing.Union[MetaOapg.properties.fte, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["notifyBy"]) -> typing.Union[MetaOapg.properties.notifyBy, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["companyInsiderTypes"]) -> typing.Union[MetaOapg.properties.companyInsiderTypes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["firstDayOfWork"]) -> typing.Union[MetaOapg.properties.firstDayOfWork, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["defaultWeeklyHours"]) -> typing.Union[MetaOapg.properties.defaultWeeklyHours, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["positionWorkerType"]) -> typing.Union['PositionWorkerType05d4c45042b610001030ee47f2c90118', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workingFte"]) -> typing.Union[MetaOapg.properties.workingFte, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["specifyWorkingFte"]) -> typing.Union[MetaOapg.properties.specifyWorkingFte, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["timeType"]) -> typing.Union['TimeType05d4c45042b610000bb540b7458e0108', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["specifyPaidFte"]) -> typing.Union[MetaOapg.properties.specifyPaidFte, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["paidFte"]) -> typing.Union[MetaOapg.properties.paidFte, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workStudy"]) -> typing.Union['WorkStudy05d4c45042b610000ba2f83c70f30101', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["assignmentType"]) -> typing.Union['AssignmentType23929e1f68ca10000d6940d6bde56963', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["endEmploymentDate"]) -> typing.Union[MetaOapg.properties.endEmploymentDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["expectedAssignmentEndDate"]) -> typing.Union[MetaOapg.properties.expectedAssignmentEndDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payRateType", "workersCompensationCodeOverride", "fte", "notifyBy", "companyInsiderTypes", "firstDayOfWork", "defaultWeeklyHours", "positionWorkerType", "workingFte", "specifyWorkingFte", "timeType", "specifyPaidFte", "paidFte", "workStudy", "assignmentType", "endEmploymentDate", "expectedAssignmentEndDate", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                payRateType: typing.Union['PayRateTypeD25283821c01100016756a14eb650000', schemas.Unset] = schemas.unset,
                workersCompensationCodeOverride: typing.Union['WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f', schemas.Unset] = schemas.unset,
                fte: typing.Union[MetaOapg.properties.fte, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                notifyBy: typing.Union[MetaOapg.properties.notifyBy, str, date, schemas.Unset] = schemas.unset,
                companyInsiderTypes: typing.Union[MetaOapg.properties.companyInsiderTypes, list, tuple, schemas.Unset] = schemas.unset,
                firstDayOfWork: typing.Union[MetaOapg.properties.firstDayOfWork, str, date, schemas.Unset] = schemas.unset,
                defaultWeeklyHours: typing.Union[MetaOapg.properties.defaultWeeklyHours, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                positionWorkerType: typing.Union['PositionWorkerType05d4c45042b610001030ee47f2c90118', schemas.Unset] = schemas.unset,
                workingFte: typing.Union[MetaOapg.properties.workingFte, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                specifyWorkingFte: typing.Union[MetaOapg.properties.specifyWorkingFte, bool, schemas.Unset] = schemas.unset,
                timeType: typing.Union['TimeType05d4c45042b610000bb540b7458e0108', schemas.Unset] = schemas.unset,
                specifyPaidFte: typing.Union[MetaOapg.properties.specifyPaidFte, bool, schemas.Unset] = schemas.unset,
                paidFte: typing.Union[MetaOapg.properties.paidFte, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                workStudy: typing.Union['WorkStudy05d4c45042b610000ba2f83c70f30101', schemas.Unset] = schemas.unset,
                assignmentType: typing.Union['AssignmentType23929e1f68ca10000d6940d6bde56963', schemas.Unset] = schemas.unset,
                endEmploymentDate: typing.Union[MetaOapg.properties.endEmploymentDate, str, date, schemas.Unset] = schemas.unset,
                expectedAssignmentEndDate: typing.Union[MetaOapg.properties.expectedAssignmentEndDate, str, date, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    payRateType=payRateType,
                    workersCompensationCodeOverride=workersCompensationCodeOverride,
                    fte=fte,
                    notifyBy=notifyBy,
                    companyInsiderTypes=companyInsiderTypes,
                    firstDayOfWork=firstDayOfWork,
                    defaultWeeklyHours=defaultWeeklyHours,
                    positionWorkerType=positionWorkerType,
                    workingFte=workingFte,
                    specifyWorkingFte=specifyWorkingFte,
                    timeType=timeType,
                    specifyPaidFte=specifyPaidFte,
                    paidFte=paidFte,
                    workStudy=workStudy,
                    assignmentType=assignmentType,
                    endEmploymentDate=endEmploymentDate,
                    expectedAssignmentEndDate=expectedAssignmentEndDate,
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
    ) -> 'ChangeJobAdministrativeDetailsDataF8f20079bc5a1000089ccb7f6a8800ea':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.assignment_type23929e1f68ca10000d6940d6bde56963 import AssignmentType23929e1f68ca10000d6940d6bde56963
from workday_staffing_python_sdk.model.change_job_company_insider_types_data05d4c45042b61000131e4b2132f30137 import ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137
from workday_staffing_python_sdk.model.pay_rate_type_d25283821c01100016756a14eb650000 import PayRateTypeD25283821c01100016756a14eb650000
from workday_staffing_python_sdk.model.position_worker_type05d4c45042b610001030ee47f2c90118 import PositionWorkerType05d4c45042b610001030ee47f2c90118
from workday_staffing_python_sdk.model.time_type05d4c45042b610000bb540b7458e0108 import TimeType05d4c45042b610000bb540b7458e0108
from workday_staffing_python_sdk.model.work_study05d4c45042b610000ba2f83c70f30101 import WorkStudy05d4c45042b610000ba2f83c70f30101
from workday_staffing_python_sdk.model.workers_compensation_code_override05d4c45042b61000138500e185e0013f import WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f