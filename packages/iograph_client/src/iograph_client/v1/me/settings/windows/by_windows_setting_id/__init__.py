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
	from .instances import InstancesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.windows_setting import WindowsSetting
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByWindowsSettingIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/settings/windows/{windowsSetting%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsSetting:
		"""
		Get windowsSetting
		Read the properties and relationships of a windowsSetting object by passing the ID of the setting in the URL. This method gets the setting for the signed-in user.
		Find more info here: https://learn.microsoft.com/graph/api/windowssetting-get?view=graph-rest-1.0
		"""
		tags = ['me.userSettings']

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
		return await self.request_adapter.send_async(request_info, WindowsSetting, error_mapping)

	async def patch(
		self,
		body: WindowsSetting,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsSetting:
		"""
		Update the navigation property windows in me
		
		"""
		tags = ['me.userSettings']

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
		return await self.request_adapter.send_async(request_info, WindowsSetting, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property windows for me
		
		"""
		tags = ['me.userSettings']
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



	def with_url(self, raw_url: str) -> ByWindowsSettingIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWindowsSettingIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWindowsSettingIdRequest(self.request_adapter, self.path_parameters)

	def instances(self,
		windowsSetting_id: str,
	) -> InstancesRequest:
		if windowsSetting_id is None:
			raise TypeError("windowsSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsSetting%2Did"] =  windowsSetting_id

		from .instances import InstancesRequest
		return InstancesRequest(self.request_adapter, path_parameters)

