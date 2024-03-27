# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from workday_staffing_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from workday_staffing_python_sdk.api_response import AsyncGeneratorResponse
from workday_staffing_python_sdk import api_client, exceptions
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

from workday_staffing_python_sdk.model.multipleinstancemodelreference import MULTIPLEINSTANCEMODELREFERENCE as MULTIPLEINSTANCEMODELREFERENCESchema
from workday_staffing_python_sdk.model.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCESchema
from workday_staffing_python_sdk.model.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCESchema

from workday_staffing_python_sdk.type.errormodelreference import ERRORMODELREFERENCE
from workday_staffing_python_sdk.type.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE
from workday_staffing_python_sdk.type.multipleinstancemodelreference import MULTIPLEINSTANCEMODELREFERENCE

from ...api_client import Dictionary
from workday_staffing_python_sdk.pydantic.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCEPydantic
from workday_staffing_python_sdk.pydantic.multipleinstancemodelreference import MULTIPLEINSTANCEMODELREFERENCE as MULTIPLEINSTANCEMODELREFERENCEPydantic
from workday_staffing_python_sdk.pydantic.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCEPydantic

from . import path

# Query params
EffectiveDateSchema = schemas.DateSchema
JobSchema = schemas.StrSchema
LimitSchema = schemas.Int64Schema
LocationSchema = schemas.StrSchema
OffsetSchema = schemas.Int64Schema


class ProposedManagerSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProposedManagerSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
StaffingEventSchema = schemas.StrSchema
WorkerSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'effectiveDate': typing.Union[EffectiveDateSchema, str, date, ],
        'job': typing.Union[JobSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'location': typing.Union[LocationSchema, str, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'proposedManager': typing.Union[ProposedManagerSchema, list, tuple, ],
        'staffingEvent': typing.Union[StaffingEventSchema, str, ],
        'worker': typing.Union[WorkerSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_effective_date = api_client.QueryParameter(
    name="effectiveDate",
    style=api_client.ParameterStyle.FORM,
    schema=EffectiveDateSchema,
    explode=True,
)
request_query_job = api_client.QueryParameter(
    name="job",
    style=api_client.ParameterStyle.FORM,
    schema=JobSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_location = api_client.QueryParameter(
    name="location",
    style=api_client.ParameterStyle.FORM,
    schema=LocationSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_proposed_manager = api_client.QueryParameter(
    name="proposedManager",
    style=api_client.ParameterStyle.FORM,
    schema=ProposedManagerSchema,
    explode=True,
)
request_query_staffing_event = api_client.QueryParameter(
    name="staffingEvent",
    style=api_client.ParameterStyle.FORM,
    schema=StaffingEventSchema,
    explode=True,
)
request_query_worker = api_client.QueryParameter(
    name="worker",
    style=api_client.ParameterStyle.FORM,
    schema=WorkerSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = MULTIPLEINSTANCEMODELREFERENCESchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MULTIPLEINSTANCEMODELREFERENCE


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MULTIPLEINSTANCEMODELREFERENCE


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = VALIDATIONERRORMODELREFERENCESchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: VALIDATIONERRORMODELREFERENCE


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ERRORMODELREFERENCESchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ERRORMODELREFERENCE


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ERRORMODELREFERENCE


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_instances_14_mapped_args(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if effective_date is not None:
            _query_params["effectiveDate"] = effective_date
        if job is not None:
            _query_params["job"] = job
        if limit is not None:
            _query_params["limit"] = limit
        if location is not None:
            _query_params["location"] = location
        if offset is not None:
            _query_params["offset"] = offset
        if proposed_manager is not None:
            _query_params["proposedManager"] = proposed_manager
        if staffing_event is not None:
            _query_params["staffingEvent"] = staffing_event
        if worker is not None:
            _query_params["worker"] = worker
        args.query = _query_params
        return args

    async def _aget_instances_14_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_effective_date,
            request_query_job,
            request_query_limit,
            request_query_location,
            request_query_offset,
            request_query_proposed_manager,
            request_query_staffing_event,
            request_query_worker,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/values/jobChangesGroup/workStudyAwards',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_instances_14_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_effective_date,
            request_query_job,
            request_query_limit,
            request_query_location,
            request_query_offset,
            request_query_proposed_manager,
            request_query_staffing_event,
            request_query_worker,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/values/jobChangesGroup/workStudyAwards',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetInstances14Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_instances_14(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_instances_14_mapped_args(
            effective_date=effective_date,
            job=job,
            limit=limit,
            location=location,
            offset=offset,
            proposed_manager=proposed_manager,
            staffing_event=staffing_event,
            worker=worker,
        )
        return await self._aget_instances_14_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_instances_14(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_instances_14_mapped_args(
            effective_date=effective_date,
            job=job,
            limit=limit,
            location=location,
            offset=offset,
            proposed_manager=proposed_manager,
            staffing_event=staffing_event,
            worker=worker,
        )
        return self._get_instances_14_oapg(
            query_params=args.query,
        )

class GetInstances14(BaseApi):

    async def aget_instances_14(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> MULTIPLEINSTANCEMODELREFERENCEPydantic:
        raw_response = await self.raw.aget_instances_14(
            effective_date=effective_date,
            job=job,
            limit=limit,
            location=location,
            offset=offset,
            proposed_manager=proposed_manager,
            staffing_event=staffing_event,
            worker=worker,
            **kwargs,
        )
        if validate:
            return MULTIPLEINSTANCEMODELREFERENCEPydantic(**raw_response.body)
        return api_client.construct_model_instance(MULTIPLEINSTANCEMODELREFERENCEPydantic, raw_response.body)
    
    
    def get_instances_14(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
        validate: bool = False,
    ) -> MULTIPLEINSTANCEMODELREFERENCEPydantic:
        raw_response = self.raw.get_instances_14(
            effective_date=effective_date,
            job=job,
            limit=limit,
            location=location,
            offset=offset,
            proposed_manager=proposed_manager,
            staffing_event=staffing_event,
            worker=worker,
        )
        if validate:
            return MULTIPLEINSTANCEMODELREFERENCEPydantic(**raw_response.body)
        return api_client.construct_model_instance(MULTIPLEINSTANCEMODELREFERENCEPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_instances_14_mapped_args(
            effective_date=effective_date,
            job=job,
            limit=limit,
            location=location,
            offset=offset,
            proposed_manager=proposed_manager,
            staffing_event=staffing_event,
            worker=worker,
        )
        return await self._aget_instances_14_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        effective_date: typing.Optional[date] = None,
        job: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        proposed_manager: typing.Optional[typing.List[str]] = None,
        staffing_event: typing.Optional[str] = None,
        worker: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_instances_14_mapped_args(
            effective_date=effective_date,
            job=job,
            limit=limit,
            location=location,
            offset=offset,
            proposed_manager=proposed_manager,
            staffing_event=staffing_event,
            worker=worker,
        )
        return self._get_instances_14_oapg(
            query_params=args.query,
        )

