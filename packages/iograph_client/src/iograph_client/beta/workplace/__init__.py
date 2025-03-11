# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sensor_devices_with_deviceid import SensorDevicesWithDeviceIdRequest
	from .sensor_devices import SensorDevicesRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.workplace import Workplace
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class WorkplaceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/workplace", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Workplace:
		"""
		Get workplace
		
		"""
		tags = ['workplace.workplace']

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
		return await self.request_adapter.send_async(request_info, Workplace, error_mapping)

	async def patch(
		self,
		body: Workplace,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Workplace:
		"""
		Update workplace
		
		"""
		tags = ['workplace.workplace']

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
		return await self.request_adapter.send_async(request_info, Workplace, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> WorkplaceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: WorkplaceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return WorkplaceRequest(self.request_adapter, self.path_parameters)

	@property
	def sensor_devices(self,
	) -> SensorDevicesRequest:
		from .sensor_devices import SensorDevicesRequest
		return SensorDevicesRequest(self.request_adapter, self.path_parameters)

	def sensor_devices_with_deviceid(self,
		deviceId: str,
	) -> SensorDevicesWithDeviceIdRequest:
		if deviceId is None:
			raise TypeError("deviceId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceId"] =  deviceId

		from .sensor_devices_with_deviceid import SensorDevicesWithDeviceIdRequest
		return SensorDevicesWithDeviceIdRequest(self.request_adapter, path_parameters)

