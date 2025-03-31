# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sync import SyncRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_autopilot_settings import WindowsAutopilotSettings
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class WindowsAutopilotSettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsAutopilotSettings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsAutopilotSettings:
		"""
		Get windowsAutopilotSettings from deviceManagement
		The Windows autopilot account settings.
		"""
		tags = ['deviceManagement.windowsAutopilotSettings']

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
		return await self.request_adapter.send_async(request_info, WindowsAutopilotSettings, error_mapping)

	async def patch(
		self,
		body: WindowsAutopilotSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsAutopilotSettings:
		"""
		Update the navigation property windowsAutopilotSettings in deviceManagement
		
		"""
		tags = ['deviceManagement.windowsAutopilotSettings']

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
		return await self.request_adapter.send_async(request_info, WindowsAutopilotSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property windowsAutopilotSettings for deviceManagement
		
		"""
		tags = ['deviceManagement.windowsAutopilotSettings']
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



	def with_url(self, raw_url: str) -> WindowsAutopilotSettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: WindowsAutopilotSettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return WindowsAutopilotSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def sync(self,
	) -> SyncRequest:
		from .sync import SyncRequest
		return SyncRequest(self.request_adapter, self.path_parameters)

