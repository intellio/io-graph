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
	from .settings import SettingsRequest
	from .setting_definitions import SettingDefinitionsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_intent_setting_category import DeviceManagementIntentSettingCategory
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementIntentSettingCategoryIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/intents/{deviceManagementIntent%2Did}/categories/{deviceManagementIntentSettingCategory%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementIntentSettingCategory:
		"""
		Get categories from deviceManagement
		Collection of setting categories within the intent
		"""
		tags = ['deviceManagement.deviceManagementIntent']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementIntentSettingCategory, error_mapping)

	async def patch(
		self,
		body: DeviceManagementIntentSettingCategory,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementIntentSettingCategory:
		"""
		Update the navigation property categories in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementIntent']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementIntentSettingCategory, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property categories for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementIntent']
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



	def with_url(self, raw_url: str) -> ByDeviceManagementIntentSettingCategoryIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementIntentSettingCategoryIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementIntentSettingCategoryIdRequest(self.request_adapter, self.path_parameters)

	def setting_definitions(self,
		deviceManagementIntent_id: str,
		deviceManagementIntentSettingCategory_id: str,
	) -> SettingDefinitionsRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")
		if deviceManagementIntentSettingCategory_id is None:
			raise TypeError("deviceManagementIntentSettingCategory_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id
		path_parameters["deviceManagementIntentSettingCategory%2Did"] =  deviceManagementIntentSettingCategory_id

		from .setting_definitions import SettingDefinitionsRequest
		return SettingDefinitionsRequest(self.request_adapter, path_parameters)

	def settings(self,
		deviceManagementIntent_id: str,
		deviceManagementIntentSettingCategory_id: str,
	) -> SettingsRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")
		if deviceManagementIntentSettingCategory_id is None:
			raise TypeError("deviceManagementIntentSettingCategory_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id
		path_parameters["deviceManagementIntentSettingCategory%2Did"] =  deviceManagementIntentSettingCategory_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

