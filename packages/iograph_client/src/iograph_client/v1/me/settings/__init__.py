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
	from .windows import WindowsRequest
	from .storage import StorageRequest
	from .shift_preferences import ShiftPreferencesRequest
	from .item_insights import ItemInsightsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.user_settings import UserSettings
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/settings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserSettings:
		"""
		Get settings
		Read the user and organization userSettings object.
To learn how to update the properties of the userSettings object, see update user settings.
		Find more info here: https://learn.microsoft.com/graph/api/usersettings-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, UserSettings, error_mapping)

	async def patch(
		self,
		body: UserSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserSettings:
		"""
		Update userSettings
		Update the properties of the userSettings object. 
Users in the same organization can have different settings based on their preference or on the organization policies. 
To get the user current settings, see current user settings. 
		Find more info here: https://learn.microsoft.com/graph/api/usersettings-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, UserSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property settings for me
		
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



	def with_url(self, raw_url: str) -> SettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def item_insights(self,
	) -> ItemInsightsRequest:
		from .item_insights import ItemInsightsRequest
		return ItemInsightsRequest(self.request_adapter, self.path_parameters)

	@property
	def shift_preferences(self,
	) -> ShiftPreferencesRequest:
		from .shift_preferences import ShiftPreferencesRequest
		return ShiftPreferencesRequest(self.request_adapter, self.path_parameters)

	@property
	def storage(self,
	) -> StorageRequest:
		from .storage import StorageRequest
		return StorageRequest(self.request_adapter, self.path_parameters)

	@property
	def windows(self,
	) -> WindowsRequest:
		from .windows import WindowsRequest
		return WindowsRequest(self.request_adapter, self.path_parameters)

