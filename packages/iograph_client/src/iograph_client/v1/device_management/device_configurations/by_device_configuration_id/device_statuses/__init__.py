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
	from .by_device_configuration_device_status_id import ByDeviceConfigurationDeviceStatusIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.device_configuration_device_status import DeviceConfigurationDeviceStatus
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.device_configuration_device_status_collection_response import DeviceConfigurationDeviceStatusCollectionResponse


class DeviceStatusesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceConfigurations/{deviceConfiguration%2Did}/deviceStatuses", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceConfigurationDeviceStatusCollectionResponse:
		"""
		List deviceConfigurationDeviceStatuses
		List properties and relationships of the deviceConfigurationDeviceStatus objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-deviceconfigurationdevicestatus-list?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceConfigurationDeviceStatusCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceConfigurationDeviceStatus,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceConfigurationDeviceStatus:
		"""
		Create deviceConfigurationDeviceStatus
		Create a new deviceConfigurationDeviceStatus object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-deviceconfigurationdevicestatus-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceConfigurationDeviceStatus, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceStatusesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceStatusesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceStatusesRequest(self.request_adapter, self.path_parameters)

	def by_device_configuration_device_status_id(self,
		deviceConfiguration_id: str,
		deviceConfigurationDeviceStatus_id: str,
	) -> ByDeviceConfigurationDeviceStatusIdRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")
		if deviceConfigurationDeviceStatus_id is None:
			raise TypeError("deviceConfigurationDeviceStatus_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id
		path_parameters["deviceConfigurationDeviceStatus%2Did"] =  deviceConfigurationDeviceStatus_id

		from .by_device_configuration_device_status_id import ByDeviceConfigurationDeviceStatusIdRequest
		return ByDeviceConfigurationDeviceStatusIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceConfiguration_id: str,
	) -> CountRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

