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


class JobProfileDetailView7deab99f645f10000bd5e61a1b780041(
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
                    summary = schemas.StrSchema
                    jobDescription = schemas.StrSchema
                    inactive = schemas.BoolSchema
                    public = schemas.BoolSchema
                
                    @staticmethod
                    def jobLevel() -> typing.Type['JobLevel89a0b59e7cce1000074acb3c1e8e015d']:
                        return JobLevel89a0b59e7cce1000074acb3c1e8e015d
                
                    @staticmethod
                    def managementLevel() -> typing.Type['ManagementLevel89a0b59e7cce1000074acb1d768e0158']:
                        return ManagementLevel89a0b59e7cce1000074acb1d768e0158
                    criticalJob = schemas.BoolSchema
                    
                    
                    class jobExempts(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['JobProfileExemptRelatedView3b00708994e41000076da515387812a2']:
                                return JobProfileExemptRelatedView3b00708994e41000076da515387812a2
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['JobProfileExemptRelatedView3b00708994e41000076da515387812a2'], typing.List['JobProfileExemptRelatedView3b00708994e41000076da515387812a2']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'jobExempts':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'JobProfileExemptRelatedView3b00708994e41000076da515387812a2':
                            return super().__getitem__(i)
                    
                    
                    class companyInsiderTypes(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CompanyInsiderTypeRelatedView7deab99f645f10001000f8a388740081']:
                                return CompanyInsiderTypeRelatedView7deab99f645f10001000f8a388740081
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CompanyInsiderTypeRelatedView7deab99f645f10001000f8a388740081'], typing.List['CompanyInsiderTypeRelatedView7deab99f645f10001000f8a388740081']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'companyInsiderTypes':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CompanyInsiderTypeRelatedView7deab99f645f10001000f8a388740081':
                            return super().__getitem__(i)
                    defaultJobTitle = schemas.StrSchema
                    workShiftRequired = schemas.BoolSchema
                    additionalJobDescription = schemas.StrSchema
                    
                    
                    class jobFamilies(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['JobFamilyRelatedView3b00708994e410000e0e2540529b12d6']:
                                return JobFamilyRelatedView3b00708994e410000e0e2540529b12d6
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['JobFamilyRelatedView3b00708994e410000e0e2540529b12d6'], typing.List['JobFamilyRelatedView3b00708994e410000e0e2540529b12d6']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'jobFamilies':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'JobFamilyRelatedView3b00708994e410000e0e2540529b12d6':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def difficultyToFill() -> typing.Type['DifficultyToFill89a0b59e7cce1000074acb57c0c50162']:
                        return DifficultyToFill89a0b59e7cce1000074acb57c0c50162
                    name = schemas.StrSchema
                
                    @staticmethod
                    def jobCategory() -> typing.Type['JobCategory89a0b59e7cce1000074acb471919015f']:
                        return JobCategory89a0b59e7cce1000074acb471919015f
                    
                    
                    class payRateTypes(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['JobProfilePayRateTypeRelatedView3b00708994e4100008d4b09e903f12b5']:
                                return JobProfilePayRateTypeRelatedView3b00708994e4100008d4b09e903f12b5
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['JobProfilePayRateTypeRelatedView3b00708994e4100008d4b09e903f12b5'], typing.List['JobProfilePayRateTypeRelatedView3b00708994e4100008d4b09e903f12b5']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'payRateTypes':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'JobProfilePayRateTypeRelatedView3b00708994e4100008d4b09e903f12b5':
                            return super().__getitem__(i)
                    
                    
                    class restrictedToCountries(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CountryRelatedView7deab99f645f10000cf305c30e260054']:
                                return CountryRelatedView7deab99f645f10000cf305c30e260054
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CountryRelatedView7deab99f645f10000cf305c30e260054'], typing.List['CountryRelatedView7deab99f645f10000cf305c30e260054']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'restrictedToCountries':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CountryRelatedView7deab99f645f10000cf305c30e260054':
                            return super().__getitem__(i)
                    
                    
                    class workersCompensationCodes(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['WorkersCompensationCodeRelatedView3b00708994e4100004af13d958811287']:
                                return WorkersCompensationCodeRelatedView3b00708994e4100004af13d958811287
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['WorkersCompensationCodeRelatedView3b00708994e4100004af13d958811287'], typing.List['WorkersCompensationCodeRelatedView3b00708994e4100004af13d958811287']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'workersCompensationCodes':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'WorkersCompensationCodeRelatedView3b00708994e4100004af13d958811287':
                            return super().__getitem__(i)
                    id = schemas.StrSchema
                    __annotations__ = {
                        "summary": summary,
                        "jobDescription": jobDescription,
                        "inactive": inactive,
                        "public": public,
                        "jobLevel": jobLevel,
                        "managementLevel": managementLevel,
                        "criticalJob": criticalJob,
                        "jobExempts": jobExempts,
                        "companyInsiderTypes": companyInsiderTypes,
                        "defaultJobTitle": defaultJobTitle,
                        "workShiftRequired": workShiftRequired,
                        "additionalJobDescription": additionalJobDescription,
                        "jobFamilies": jobFamilies,
                        "difficultyToFill": difficultyToFill,
                        "name": name,
                        "jobCategory": jobCategory,
                        "payRateTypes": payRateTypes,
                        "restrictedToCountries": restrictedToCountries,
                        "workersCompensationCodes": workersCompensationCodes,
                        "id": id,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobDescription"]) -> MetaOapg.properties.jobDescription: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inactive"]) -> MetaOapg.properties.inactive: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobLevel"]) -> 'JobLevel89a0b59e7cce1000074acb3c1e8e015d': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["managementLevel"]) -> 'ManagementLevel89a0b59e7cce1000074acb1d768e0158': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["criticalJob"]) -> MetaOapg.properties.criticalJob: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobExempts"]) -> MetaOapg.properties.jobExempts: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["companyInsiderTypes"]) -> MetaOapg.properties.companyInsiderTypes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["defaultJobTitle"]) -> MetaOapg.properties.defaultJobTitle: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workShiftRequired"]) -> MetaOapg.properties.workShiftRequired: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["additionalJobDescription"]) -> MetaOapg.properties.additionalJobDescription: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobFamilies"]) -> MetaOapg.properties.jobFamilies: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["difficultyToFill"]) -> 'DifficultyToFill89a0b59e7cce1000074acb57c0c50162': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobCategory"]) -> 'JobCategory89a0b59e7cce1000074acb471919015f': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["payRateTypes"]) -> MetaOapg.properties.payRateTypes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["restrictedToCountries"]) -> MetaOapg.properties.restrictedToCountries: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workersCompensationCodes"]) -> MetaOapg.properties.workersCompensationCodes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "jobDescription", "inactive", "public", "jobLevel", "managementLevel", "criticalJob", "jobExempts", "companyInsiderTypes", "defaultJobTitle", "workShiftRequired", "additionalJobDescription", "jobFamilies", "difficultyToFill", "name", "jobCategory", "payRateTypes", "restrictedToCountries", "workersCompensationCodes", "id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobDescription"]) -> typing.Union[MetaOapg.properties.jobDescription, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inactive"]) -> typing.Union[MetaOapg.properties.inactive, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> typing.Union[MetaOapg.properties.public, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobLevel"]) -> typing.Union['JobLevel89a0b59e7cce1000074acb3c1e8e015d', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["managementLevel"]) -> typing.Union['ManagementLevel89a0b59e7cce1000074acb1d768e0158', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["criticalJob"]) -> typing.Union[MetaOapg.properties.criticalJob, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobExempts"]) -> typing.Union[MetaOapg.properties.jobExempts, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["companyInsiderTypes"]) -> typing.Union[MetaOapg.properties.companyInsiderTypes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["defaultJobTitle"]) -> typing.Union[MetaOapg.properties.defaultJobTitle, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workShiftRequired"]) -> typing.Union[MetaOapg.properties.workShiftRequired, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["additionalJobDescription"]) -> typing.Union[MetaOapg.properties.additionalJobDescription, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobFamilies"]) -> typing.Union[MetaOapg.properties.jobFamilies, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["difficultyToFill"]) -> typing.Union['DifficultyToFill89a0b59e7cce1000074acb57c0c50162', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobCategory"]) -> typing.Union['JobCategory89a0b59e7cce1000074acb471919015f', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["payRateTypes"]) -> typing.Union[MetaOapg.properties.payRateTypes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["restrictedToCountries"]) -> typing.Union[MetaOapg.properties.restrictedToCountries, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workersCompensationCodes"]) -> typing.Union[MetaOapg.properties.workersCompensationCodes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "jobDescription", "inactive", "public", "jobLevel", "managementLevel", "criticalJob", "jobExempts", "companyInsiderTypes", "defaultJobTitle", "workShiftRequired", "additionalJobDescription", "jobFamilies", "difficultyToFill", "name", "jobCategory", "payRateTypes", "restrictedToCountries", "workersCompensationCodes", "id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                summary: typing.Union[MetaOapg.properties.summary, str, schemas.Unset] = schemas.unset,
                jobDescription: typing.Union[MetaOapg.properties.jobDescription, str, schemas.Unset] = schemas.unset,
                inactive: typing.Union[MetaOapg.properties.inactive, bool, schemas.Unset] = schemas.unset,
                public: typing.Union[MetaOapg.properties.public, bool, schemas.Unset] = schemas.unset,
                jobLevel: typing.Union['JobLevel89a0b59e7cce1000074acb3c1e8e015d', schemas.Unset] = schemas.unset,
                managementLevel: typing.Union['ManagementLevel89a0b59e7cce1000074acb1d768e0158', schemas.Unset] = schemas.unset,
                criticalJob: typing.Union[MetaOapg.properties.criticalJob, bool, schemas.Unset] = schemas.unset,
                jobExempts: typing.Union[MetaOapg.properties.jobExempts, list, tuple, schemas.Unset] = schemas.unset,
                companyInsiderTypes: typing.Union[MetaOapg.properties.companyInsiderTypes, list, tuple, schemas.Unset] = schemas.unset,
                defaultJobTitle: typing.Union[MetaOapg.properties.defaultJobTitle, str, schemas.Unset] = schemas.unset,
                workShiftRequired: typing.Union[MetaOapg.properties.workShiftRequired, bool, schemas.Unset] = schemas.unset,
                additionalJobDescription: typing.Union[MetaOapg.properties.additionalJobDescription, str, schemas.Unset] = schemas.unset,
                jobFamilies: typing.Union[MetaOapg.properties.jobFamilies, list, tuple, schemas.Unset] = schemas.unset,
                difficultyToFill: typing.Union['DifficultyToFill89a0b59e7cce1000074acb57c0c50162', schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                jobCategory: typing.Union['JobCategory89a0b59e7cce1000074acb471919015f', schemas.Unset] = schemas.unset,
                payRateTypes: typing.Union[MetaOapg.properties.payRateTypes, list, tuple, schemas.Unset] = schemas.unset,
                restrictedToCountries: typing.Union[MetaOapg.properties.restrictedToCountries, list, tuple, schemas.Unset] = schemas.unset,
                workersCompensationCodes: typing.Union[MetaOapg.properties.workersCompensationCodes, list, tuple, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    summary=summary,
                    jobDescription=jobDescription,
                    inactive=inactive,
                    public=public,
                    jobLevel=jobLevel,
                    managementLevel=managementLevel,
                    criticalJob=criticalJob,
                    jobExempts=jobExempts,
                    companyInsiderTypes=companyInsiderTypes,
                    defaultJobTitle=defaultJobTitle,
                    workShiftRequired=workShiftRequired,
                    additionalJobDescription=additionalJobDescription,
                    jobFamilies=jobFamilies,
                    difficultyToFill=difficultyToFill,
                    name=name,
                    jobCategory=jobCategory,
                    payRateTypes=payRateTypes,
                    restrictedToCountries=restrictedToCountries,
                    workersCompensationCodes=workersCompensationCodes,
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
    ) -> 'JobProfileDetailView7deab99f645f10000bd5e61a1b780041':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from workday_staffing_python_sdk.model.company_insider_type_related_view7deab99f645f10001000f8a388740081 import CompanyInsiderTypeRelatedView7deab99f645f10001000f8a388740081
from workday_staffing_python_sdk.model.country_related_view7deab99f645f10000cf305c30e260054 import CountryRelatedView7deab99f645f10000cf305c30e260054
from workday_staffing_python_sdk.model.difficulty_to_fill89a0b59e7cce1000074acb57c0c50162 import DifficultyToFill89a0b59e7cce1000074acb57c0c50162
from workday_staffing_python_sdk.model.job_category89a0b59e7cce1000074acb471919015f import JobCategory89a0b59e7cce1000074acb471919015f
from workday_staffing_python_sdk.model.job_family_related_view3b00708994e410000e0e2540529b12d6 import JobFamilyRelatedView3b00708994e410000e0e2540529b12d6
from workday_staffing_python_sdk.model.job_level89a0b59e7cce1000074acb3c1e8e015d import JobLevel89a0b59e7cce1000074acb3c1e8e015d
from workday_staffing_python_sdk.model.job_profile_exempt_related_view3b00708994e41000076da515387812a2 import JobProfileExemptRelatedView3b00708994e41000076da515387812a2
from workday_staffing_python_sdk.model.job_profile_pay_rate_type_related_view3b00708994e4100008d4b09e903f12b5 import JobProfilePayRateTypeRelatedView3b00708994e4100008d4b09e903f12b5
from workday_staffing_python_sdk.model.management_level89a0b59e7cce1000074acb1d768e0158 import ManagementLevel89a0b59e7cce1000074acb1d768e0158
from workday_staffing_python_sdk.model.workers_compensation_code_related_view3b00708994e4100004af13d958811287 import WorkersCompensationCodeRelatedView3b00708994e4100004af13d958811287
