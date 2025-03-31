# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .setting_definitions import SettingDefinitionsRequest
	from .recommended_settings import RecommendedSettingsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_template_setting_category import DeviceManagementTemplateSettingCategory
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementTemplateSettingCategoryIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/templates/{deviceManagementTemplate%2Did}/migratableTo/{deviceManagementTemplate%2Did1}/categories/{deviceManagementTemplateSettingCategory%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementTemplateSettingCategory:
		"""
		Get categories from deviceManagement
		Collection of setting categories within the template
		"""
		tags = ['deviceManagement.deviceManagementTemplate']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplateSettingCategory, error_mapping)

	async def patch(
		self,
		body: DeviceManagementTemplateSettingCategory,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementTemplateSettingCategory:
		"""
		Update the navigation property categories in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementTemplate']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplateSettingCategory, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property categories for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementTemplate']
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



	def with_url(self, raw_url: str) -> ByDeviceManagementTemplateSettingCategoryIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementTemplateSettingCategoryIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementTemplateSettingCategoryIdRequest(self.request_adapter, self.path_parameters)

	def recommended_settings(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
		deviceManagementTemplateSettingCategory_id: str,
	) -> RecommendedSettingsRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")
		if deviceManagementTemplateSettingCategory_id is None:
			raise TypeError("deviceManagementTemplateSettingCategory_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1
		path_parameters["deviceManagementTemplateSettingCategory%2Did"] =  deviceManagementTemplateSettingCategory_id

		from .recommended_settings import RecommendedSettingsRequest
		return RecommendedSettingsRequest(self.request_adapter, path_parameters)

	def setting_definitions(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
		deviceManagementTemplateSettingCategory_id: str,
	) -> SettingDefinitionsRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")
		if deviceManagementTemplateSettingCategory_id is None:
			raise TypeError("deviceManagementTemplateSettingCategory_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1
		path_parameters["deviceManagementTemplateSettingCategory%2Did"] =  deviceManagementTemplateSettingCategory_id

		from .setting_definitions import SettingDefinitionsRequest
		return SettingDefinitionsRequest(self.request_adapter, path_parameters)

