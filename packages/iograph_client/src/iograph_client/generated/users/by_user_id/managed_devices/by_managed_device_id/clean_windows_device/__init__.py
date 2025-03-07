# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.clean_windows_device_post_request import Clean_windows_devicePostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CleanWindowsDeviceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices/{managedDevice%2Did}/cleanWindowsDevice", path_parameters)

	async def post(
		self,
		body: Clean_windows_devicePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action cleanWindowsDevice
		Clean Windows device
		Find more info here: https://learn.microsoft.com/graph/api/intune-devices-manageddevice-cleanwindowsdevice?view=graph-rest-1.0
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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> CleanWindowsDeviceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CleanWindowsDeviceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CleanWindowsDeviceRequest(self.request_adapter, self.path_parameters)

