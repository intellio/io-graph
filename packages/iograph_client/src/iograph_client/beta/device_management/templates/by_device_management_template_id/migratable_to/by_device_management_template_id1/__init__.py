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
	from .create_instance import CreateInstanceRequest
	from .compare_with_templateid import CompareWithTemplateIdRequest
	from .categories import CategoriesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_template import DeviceManagementTemplate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementTemplateId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/templates/{deviceManagementTemplate%2Did}/migratableTo/{deviceManagementTemplate%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementTemplate:
		"""
		Get migratableTo from deviceManagement
		Collection of templates this template can migrate to
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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplate, error_mapping)

	async def patch(
		self,
		body: DeviceManagementTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementTemplate:
		"""
		Update the navigation property migratableTo in deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplate, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property migratableTo for deviceManagement
		
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



	def with_url(self, raw_url: str) -> ByDeviceManagementTemplateId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementTemplateId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementTemplateId1Request(self.request_adapter, self.path_parameters)

	def categories(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
	) -> CategoriesRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1

		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, path_parameters)

	def compare_with_templateid(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
		templateId: str,
	) -> CompareWithTemplateIdRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")
		if templateId is None:
			raise TypeError("templateId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1
		path_parameters["templateId"] =  templateId

		from .compare_with_templateid import CompareWithTemplateIdRequest
		return CompareWithTemplateIdRequest(self.request_adapter, path_parameters)

	def create_instance(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
	) -> CreateInstanceRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1

		from .create_instance import CreateInstanceRequest
		return CreateInstanceRequest(self.request_adapter, path_parameters)

	def settings(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
	) -> SettingsRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

