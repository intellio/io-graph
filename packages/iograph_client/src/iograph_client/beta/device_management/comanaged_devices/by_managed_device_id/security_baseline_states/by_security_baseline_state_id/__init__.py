# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .setting_states import SettingStatesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_baseline_state import SecurityBaselineState


class BySecurityBaselineStateIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/comanagedDevices/{managedDevice%2Did}/securityBaselineStates/{securityBaselineState%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityBaselineState:
		"""
		Get securityBaselineStates from deviceManagement
		Security baseline states for this device.
		"""
		tags = ['deviceManagement.managedDevice']

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
		return await self.request_adapter.send_async(request_info, SecurityBaselineState, error_mapping)

	async def patch(
		self,
		body: SecurityBaselineState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityBaselineState:
		"""
		Update the navigation property securityBaselineStates in deviceManagement
		
		"""
		tags = ['deviceManagement.managedDevice']

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
		return await self.request_adapter.send_async(request_info, SecurityBaselineState, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property securityBaselineStates for deviceManagement
		
		"""
		tags = ['deviceManagement.managedDevice']
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



	def with_url(self, raw_url: str) -> BySecurityBaselineStateIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySecurityBaselineStateIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySecurityBaselineStateIdRequest(self.request_adapter, self.path_parameters)

	def setting_states(self,
		managedDevice_id: str,
		securityBaselineState_id: str,
	) -> SettingStatesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")
		if securityBaselineState_id is None:
			raise TypeError("securityBaselineState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id
		path_parameters["securityBaselineState%2Did"] =  securityBaselineState_id

		from .setting_states import SettingStatesRequest
		return SettingStatesRequest(self.request_adapter, path_parameters)

