# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_device_health_script_device_state_id import ByDeviceHealthScriptDeviceStateIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_health_script_device_state import DeviceHealthScriptDeviceState
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_health_script_device_state_collection_response import DeviceHealthScriptDeviceStateCollectionResponse


class DeviceRunStatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceHealthScripts/{deviceHealthScript%2Did}/deviceRunStates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceHealthScriptDeviceStateCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, DeviceHealthScriptDeviceStateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceHealthScriptDeviceState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceHealthScriptDeviceState:
		"""
		Create new navigation property to deviceRunStates for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceHealthScript']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, DeviceHealthScriptDeviceState, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceRunStatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceRunStatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceRunStatesRequest(self.request_adapter, self.path_parameters)

	def by_device_health_script_device_state_id(self,
		deviceHealthScript_id: str,
		deviceHealthScriptDeviceState_id: str,
	) -> ByDeviceHealthScriptDeviceStateIdRequest:
		if deviceHealthScript_id is None:
			raise TypeError("deviceHealthScript_id cannot be null.")
		if deviceHealthScriptDeviceState_id is None:
			raise TypeError("deviceHealthScriptDeviceState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceHealthScript%2Did"] =  deviceHealthScript_id
		path_parameters["deviceHealthScriptDeviceState%2Did"] =  deviceHealthScriptDeviceState_id

		from .by_device_health_script_device_state_id import ByDeviceHealthScriptDeviceStateIdRequest
		return ByDeviceHealthScriptDeviceStateIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceHealthScript_id: str,
	) -> CountRequest:
		if deviceHealthScript_id is None:
			raise TypeError("deviceHealthScript_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceHealthScript%2Did"] =  deviceHealthScript_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

