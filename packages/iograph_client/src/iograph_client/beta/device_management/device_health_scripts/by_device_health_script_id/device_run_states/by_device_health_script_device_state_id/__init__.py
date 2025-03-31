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
	from .managed_device import ManagedDeviceRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_health_script_device_state import DeviceHealthScriptDeviceState
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceHealthScriptDeviceStateIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceHealthScripts/{deviceHealthScript%2Did}/deviceRunStates/{deviceHealthScriptDeviceState%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceHealthScriptDeviceState:
		"""
		Get deviceRunStates from deviceManagement
		List of run states for the device health script across all devices
		"""
		tags = ['deviceManagement.deviceHealthScript']

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
		return await self.request_adapter.send_async(request_info, DeviceHealthScriptDeviceState, error_mapping)

	async def patch(
		self,
		body: DeviceHealthScriptDeviceState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceHealthScriptDeviceState:
		"""
		Update the navigation property deviceRunStates in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceHealthScript']

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
		return await self.request_adapter.send_async(request_info, DeviceHealthScriptDeviceState, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property deviceRunStates for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceHealthScript']
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



	def with_url(self, raw_url: str) -> ByDeviceHealthScriptDeviceStateIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceHealthScriptDeviceStateIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceHealthScriptDeviceStateIdRequest(self.request_adapter, self.path_parameters)

	def managed_device(self,
		deviceHealthScript_id: str,
		deviceHealthScriptDeviceState_id: str,
	) -> ManagedDeviceRequest:
		if deviceHealthScript_id is None:
			raise TypeError("deviceHealthScript_id cannot be null.")
		if deviceHealthScriptDeviceState_id is None:
			raise TypeError("deviceHealthScriptDeviceState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceHealthScript%2Did"] =  deviceHealthScript_id
		path_parameters["deviceHealthScriptDeviceState%2Did"] =  deviceHealthScriptDeviceState_id

		from .managed_device import ManagedDeviceRequest
		return ManagedDeviceRequest(self.request_adapter, path_parameters)

