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
from workday_staffing_python_sdk.model.change_job_contract_details_data27ec818d10d010000386ce823ac20107 import ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107 as ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Schema
from workday_staffing_python_sdk.model.frequency2d0ca2cb2448100009c5436d5d670e06 import Frequency2d0ca2cb2448100009c5436d5d670e06 as Frequency2d0ca2cb2448100009c5436d5d670e06Schema
from workday_staffing_python_sdk.model.purchase_order2d0ca2cb2448100009c5433bcff60e05 import PurchaseOrder2d0ca2cb2448100009c5433bcff60e05 as PurchaseOrder2d0ca2cb2448100009c5433bcff60e05Schema
from workday_staffing_python_sdk.model.currency2d0ca2cb2448100009c54386a8570e07 import Currency2d0ca2cb2448100009c54386a8570e07 as Currency2d0ca2cb2448100009c54386a8570e07Schema
from workday_staffing_python_sdk.model.errormodelreference import ERRORMODELREFERENCE as ERRORMODELREFERENCESchema

from workday_staffing_python_sdk.type.change_job_contract_details_data27ec818d10d010000386ce823ac20107 import ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107
from workday_staffing_python_sdk.type.purchase_order2d0ca2cb2448100009c5433bcff60e05 import PurchaseOrder2d0ca2cb2448100009c5433bcff60e05
from workday_staffing_python_sdk.type.errormodelreference import ERRORMODELREFERENCE
from workday_staffing_python_sdk.type.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE
from workday_staffing_python_sdk.type.frequency2d0ca2cb2448100009c5436d5d670e06 import Frequency2d0ca2cb2448100009c5436d5d670e06
from workday_staffing_python_sdk.type.currency2d0ca2cb2448100009c54386a8570e07 import Currency2d0ca2cb2448100009c54386a8570e07

from ...api_client import Dictionary
from workday_staffing_python_sdk.pydantic.purchase_order2d0ca2cb2448100009c5433bcff60e05 import PurchaseOrder2d0ca2cb2448100009c5433bcff60e05 as PurchaseOrder2d0ca2cb2448100009c5433bcff60e05Pydantic
from workday_staffing_python_sdk.pydantic.frequency2d0ca2cb2448100009c5436d5d670e06 import Frequency2d0ca2cb2448100009c5436d5d670e06 as Frequency2d0ca2cb2448100009c5436d5d670e06Pydantic
from workday_staffing_python_sdk.pydantic.validationerrormodelreference import VALIDATIONERRORMODELREFERENCE as VALIDATIONERRORMODELREFERENCEPydantic
from workday_staffing_python_sdk.pydantic.currency2d0ca2cb2448100009c54386a8570e07 import Currency2d0ca2cb2448100009c54386a8570e07 as Currency2d0ca2cb2448100009c54386a8570e07Pydantic
from workday_staffing_python_sdk.pydantic.change_job_contract_details_data27ec818d10d010000386ce823ac20107 import ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107 as ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic
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
SchemaForRequestBodyApplicationJson = ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Schema


request_body_change_job_contract_details_data27ec818d10d010000386ce823ac20107 = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Schema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107


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

    def _partially_update_contract_options_mapped_args(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if assignment_details is not None:
            _body["assignmentDetails"] = assignment_details
        if contract_end_date is not None:
            _body["contractEndDate"] = contract_end_date
        if contract_pay_rate is not None:
            _body["contractPayRate"] = contract_pay_rate
        if currency is not None:
            _body["currency"] = currency
        if frequency is not None:
            _body["frequency"] = frequency
        if purchase_order is not None:
            _body["purchaseOrder"] = purchase_order
        args.body = _body
        if id is not None:
            _path_params["ID"] = id
        if subresource_id is not None:
            _path_params["subresourceID"] = subresource_id
        args.path = _path_params
        return args

    async def _apartially_update_contract_options_oapg(
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
        Partially updates the contract options for the specified change job ID.
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
            path_template='/jobChanges/{ID}/contract/{subresourceID}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_change_job_contract_details_data27ec818d10d010000386ce823ac20107.serialize(body, content_type)
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


    def _partially_update_contract_options_oapg(
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
        Partially updates the contract options for the specified change job ID.
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
            path_template='/jobChanges/{ID}/contract/{subresourceID}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_change_job_contract_details_data27ec818d10d010000386ce823ac20107.serialize(body, content_type)
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


class PartiallyUpdateContractOptionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apartially_update_contract_options(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._partially_update_contract_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            assignment_details=assignment_details,
            contract_end_date=contract_end_date,
            contract_pay_rate=contract_pay_rate,
            currency=currency,
            frequency=frequency,
            purchase_order=purchase_order,
        )
        return await self._apartially_update_contract_options_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def partially_update_contract_options(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._partially_update_contract_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            assignment_details=assignment_details,
            contract_end_date=contract_end_date,
            contract_pay_rate=contract_pay_rate,
            currency=currency,
            frequency=frequency,
            purchase_order=purchase_order,
        )
        return self._partially_update_contract_options_oapg(
            body=args.body,
            path_params=args.path,
        )

class PartiallyUpdateContractOptions(BaseApi):

    async def apartially_update_contract_options(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
        validate: bool = False,
        **kwargs,
    ) -> ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic:
        raw_response = await self.raw.apartially_update_contract_options(
            body=body,
            id=id,
            subresource_id=subresource_id,
            assignment_details=assignment_details,
            contract_end_date=contract_end_date,
            contract_pay_rate=contract_pay_rate,
            currency=currency,
            frequency=frequency,
            purchase_order=purchase_order,
            **kwargs,
        )
        if validate:
            return RootModel[ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic](raw_response.body).root
        return api_client.construct_model_instance(ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic, raw_response.body)
    
    
    def partially_update_contract_options(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
        validate: bool = False,
    ) -> ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic:
        raw_response = self.raw.partially_update_contract_options(
            body=body,
            id=id,
            subresource_id=subresource_id,
            assignment_details=assignment_details,
            contract_end_date=contract_end_date,
            contract_pay_rate=contract_pay_rate,
            currency=currency,
            frequency=frequency,
            purchase_order=purchase_order,
        )
        if validate:
            return RootModel[ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic](raw_response.body).root
        return api_client.construct_model_instance(ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107Pydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._partially_update_contract_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            assignment_details=assignment_details,
            contract_end_date=contract_end_date,
            contract_pay_rate=contract_pay_rate,
            currency=currency,
            frequency=frequency,
            purchase_order=purchase_order,
        )
        return await self._apartially_update_contract_options_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        id: str,
        subresource_id: str,
        assignment_details: typing.Optional[str] = None,
        contract_end_date: typing.Optional[date] = None,
        contract_pay_rate: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        currency: typing.Optional[Currency2d0ca2cb2448100009c54386a8570e07] = None,
        frequency: typing.Optional[Frequency2d0ca2cb2448100009c5436d5d670e06] = None,
        purchase_order: typing.Optional[PurchaseOrder2d0ca2cb2448100009c5433bcff60e05] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._partially_update_contract_options_mapped_args(
            body=body,
            id=id,
            subresource_id=subresource_id,
            assignment_details=assignment_details,
            contract_end_date=contract_end_date,
            contract_pay_rate=contract_pay_rate,
            currency=currency,
            frequency=frequency,
            purchase_order=purchase_order,
        )
        return self._partially_update_contract_options_oapg(
            body=args.body,
            path_params=args.path,
        )

