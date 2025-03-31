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
	from .count import CountRequest
	from .by_device_configuration_state_id import ByDeviceConfigurationStateIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_configuration_state_collection_response import DeviceConfigurationStateCollectionResponse
from iograph_models.beta.device_configuration_state import DeviceConfigurationState
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceConfigurationStatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices/{managedDevice%2Did}/deviceConfigurationStates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceConfigurationStateCollectionResponse:
		"""
		Get deviceConfigurationStates from users
		Device configuration states for this device.
		"""
		tags = ['users.managedDevice']

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
		return await self.request_adapter.send_async(request_info, DeviceConfigurationStateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceConfigurationState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceConfigurationState:
		"""
		Create new navigation property to deviceConfigurationStates for users
		
		"""
		tags = ['users.managedDevice']

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
		return await self.request_adapter.send_async(request_info, DeviceConfigurationState, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceConfigurationStatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceConfigurationStatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceConfigurationStatesRequest(self.request_adapter, self.path_parameters)

	def by_device_configuration_state_id(self,
		user_id: str,
		managedDevice_id: str,
		deviceConfigurationState_id: str,
	) -> ByDeviceConfigurationStateIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")
		if deviceConfigurationState_id is None:
			raise TypeError("deviceConfigurationState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id
		path_parameters["deviceConfigurationState%2Did"] =  deviceConfigurationState_id

		from .by_device_configuration_state_id import ByDeviceConfigurationStateIdRequest
		return ByDeviceConfigurationStateIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		managedDevice_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

