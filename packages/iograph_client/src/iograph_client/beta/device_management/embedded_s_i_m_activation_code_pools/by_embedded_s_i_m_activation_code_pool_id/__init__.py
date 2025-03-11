# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .assign import AssignRequest
	from .device_states import DeviceStatesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool


class ByEmbeddedSIMActivationCodePoolIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/embeddedSIMActivationCodePools/{embeddedSIMActivationCodePool%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EmbeddedSIMActivationCodePool:
		"""
		Get embeddedSIMActivationCodePools from deviceManagement
		The embedded SIM activation code pools created by this account.
		"""
		tags = ['deviceManagement.embeddedSIMActivationCodePool']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, EmbeddedSIMActivationCodePool, error_mapping)

	async def patch(
		self,
		body: EmbeddedSIMActivationCodePool,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EmbeddedSIMActivationCodePool:
		"""
		Update the navigation property embeddedSIMActivationCodePools in deviceManagement
		
		"""
		tags = ['deviceManagement.embeddedSIMActivationCodePool']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, EmbeddedSIMActivationCodePool, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property embeddedSIMActivationCodePools for deviceManagement
		
		"""
		tags = ['deviceManagement.embeddedSIMActivationCodePool']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByEmbeddedSIMActivationCodePoolIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEmbeddedSIMActivationCodePoolIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEmbeddedSIMActivationCodePoolIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		embeddedSIMActivationCodePool_id: str,
	) -> AssignmentsRequest:
		if embeddedSIMActivationCodePool_id is None:
			raise TypeError("embeddedSIMActivationCodePool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["embeddedSIMActivationCodePool%2Did"] =  embeddedSIMActivationCodePool_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def device_states(self,
		embeddedSIMActivationCodePool_id: str,
	) -> DeviceStatesRequest:
		if embeddedSIMActivationCodePool_id is None:
			raise TypeError("embeddedSIMActivationCodePool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["embeddedSIMActivationCodePool%2Did"] =  embeddedSIMActivationCodePool_id

		from .device_states import DeviceStatesRequest
		return DeviceStatesRequest(self.request_adapter, path_parameters)

	def assign(self,
		embeddedSIMActivationCodePool_id: str,
	) -> AssignRequest:
		if embeddedSIMActivationCodePool_id is None:
			raise TypeError("embeddedSIMActivationCodePool_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["embeddedSIMActivationCodePool%2Did"] =  embeddedSIMActivationCodePool_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

