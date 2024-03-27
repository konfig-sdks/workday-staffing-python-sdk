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

from workday_staffing_python_sdk.model.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCESchema
from workday_staffing_python_sdk.model.change_job_location90151d6c4ff110001b4a46091678025c import ChangeJobLocation90151d6c4ff110001b4a46091678025c as ChangeJobLocation90151d6c4ff110001b4a46091678025cSchema
from workday_staffing_python_sdk.model.work_space0ee7bb8b41db10001e7db6a6c3e55663 import WorkSpace0ee7bb8b41db10001e7db6a6c3e55663 as WorkSpace0ee7bb8b41db10001e7db6a6c3e55663Schema
from workday_staffing_python_sdk.model.work_shift0ee7bb8b41db1000143d4e4822174f2e import WorkShift0ee7bb8b41db1000143d4e4822174f2e as WorkShift0ee7bb8b41db1000143d4e4822174f2eSchema
from workday_staffing_python_sdk.model.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCESchema
from workday_staffing_python_sdk.model.location90151d6c4ff110001bfa027116820278 import Location90151d6c4ff110001bfa027116820278 as Location90151d6c4ff110001bfa027116820278Schema

from workday_staffing_python_sdk.type.location90151d6c4ff110001bfa027116820278 import Location90151d6c4ff110001bfa027116820278
from workday_staffing_python_sdk.type.errormodelreference import ERRORMODELREFERENCE
from workday_staffing_python_sdk.type.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE
from workday_staffing_python_sdk.type.work_space0ee7bb8b41db10001e7db6a6c3e55663 import WorkSpace0ee7bb8b41db10001e7db6a6c3e55663
from workday_staffing_python_sdk.type.change_job_location90151d6c4ff110001b4a46091678025c import ChangeJobLocation90151d6c4ff110001b4a46091678025c
from workday_staffing_python_sdk.type.work_shift0ee7bb8b41db1000143d4e4822174f2e import WorkShift0ee7bb8b41db1000143d4e4822174f2e

from ...api_client import Dictionary
from workday_staffing_python_sdk.pydantic.work_shift0ee7bb8b41db1000143d4e4822174f2e import WorkShift0ee7bb8b41db1000143d4e4822174f2e as WorkShift0ee7bb8b41db1000143d4e4822174f2ePydantic
from workday_staffing_python_sdk.pydantic.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCEPydantic
from workday_staffing_python_sdk.pydantic.work_space0ee7bb8b41db10001e7db6a6c3e55663 import WorkSpace0ee7bb8b41db10001e7db6a6c3e55663 as WorkSpace0ee7bb8b41db10001e7db6a6c3e55663Pydantic
from workday_staffing_python_sdk.pydantic.location90151d6c4ff110001bfa027116820278 import Location90151d6c4ff110001bfa027116820278 as Location90151d6c4ff110001bfa027116820278Pydantic
from workday_staffing_python_sdk.pydantic.change_job_location90151d6c4ff110001b4a46091678025c import ChangeJobLocation90151d6c4ff110001b4a46091678025c as ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic
from workday_staffing_python_sdk.pydantic.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCEPydantic

from . import path

# Path params
IDSchema = schemas.StrSchema
SubresourceIDSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'ID': typing.Union[IDSchema, str, ],
        'subresourceID': typing.Union[SubresourceIDSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IDSchema,
    required=True,
)
request_path_subresource_id = api_client.PathParameter(
    name="subresourceID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SubresourceIDSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ChangeJobLocation90151d6c4ff110001b4a46091678025cSchema


request_body_change_job_location90151d6c4ff110001b4a46091678025c = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ChangeJobLocation90151d6c4ff110001b4a46091678025cSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ChangeJobLocation90151d6c4ff110001b4a46091678025c


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ChangeJobLocation90151d6c4ff110001b4a46091678025c


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

    def _partial_update_location_options_mapped_args(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if location is not None:
            _body["location"] = location
        if scheduled_hours is not None:
            _body["scheduledHours"] = scheduled_hours
        if work_shift is not None:
            _body["workShift"] = work_shift
        if work_space is not None:
            _body["workSpace"] = work_space
        args.body = _body
        if id is not None:
            _path_params["ID"] = id
        if subresource_id is not None:
            _path_params["subresourceID"] = subresource_id
        args.path = _path_params
        return args

    async def _apartial_update_location_options_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Partially updates the location options for the specified change job ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
            request_path_subresource_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/jobChanges/{ID}/location/{subresourceID}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_change_job_location90151d6c4ff110001b4a46091678025c.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _partial_update_location_options_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Partially updates the location options for the specified change job ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
            request_path_subresource_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/jobChanges/{ID}/location/{subresourceID}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_change_job_location90151d6c4ff110001b4a46091678025c.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class PartialUpdateLocationOptionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apartial_update_location_options(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._partial_update_location_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            location=location,
            scheduled_hours=scheduled_hours,
            work_shift=work_shift,
            work_space=work_space,
        )
        return await self._apartial_update_location_options_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def partial_update_location_options(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._partial_update_location_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            location=location,
            scheduled_hours=scheduled_hours,
            work_shift=work_shift,
            work_space=work_space,
        )
        return self._partial_update_location_options_oapg(
            body=args.body,
            path_params=args.path,
        )

class PartialUpdateLocationOptions(BaseApi):

    async def apartial_update_location_options(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
        validate: bool = False,
        **kwargs,
    ) -> ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic:
        raw_response = await self.raw.apartial_update_location_options(
            body=body,
            id=id,
            subresource_id=subresource_id,
            location=location,
            scheduled_hours=scheduled_hours,
            work_shift=work_shift,
            work_space=work_space,
            **kwargs,
        )
        if validate:
            return RootModel[ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic](raw_response.body).root
        return api_client.construct_model_instance(ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic, raw_response.body)
    
    
    def partial_update_location_options(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
        validate: bool = False,
    ) -> ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic:
        raw_response = self.raw.partial_update_location_options(
            body=body,
            id=id,
            subresource_id=subresource_id,
            location=location,
            scheduled_hours=scheduled_hours,
            work_shift=work_shift,
            work_space=work_space,
        )
        if validate:
            return RootModel[ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic](raw_response.body).root
        return api_client.construct_model_instance(ChangeJobLocation90151d6c4ff110001b4a46091678025cPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._partial_update_location_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            location=location,
            scheduled_hours=scheduled_hours,
            work_shift=work_shift,
            work_space=work_space,
        )
        return await self._apartial_update_location_options_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        id: str,
        subresource_id: str,
        location: typing.Optional[Location90151d6c4ff110001bfa027116820278] = None,
        scheduled_hours: typing.Optional[int] = None,
        work_shift: typing.Optional[WorkShift0ee7bb8b41db1000143d4e4822174f2e] = None,
        work_space: typing.Optional[WorkSpace0ee7bb8b41db10001e7db6a6c3e55663] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._partial_update_location_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            location=location,
            scheduled_hours=scheduled_hours,
            work_shift=work_shift,
            work_space=work_space,
        )
        return self._partial_update_location_options_oapg(
            body=args.body,
            path_params=args.path,
        )

