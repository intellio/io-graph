# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .import_office365_device_configuration_policies import ImportOffice365DeviceConfigurationPoliciesRequest
	from .count import CountRequest
	from .by_device_management_template_id import ByDeviceManagementTemplateIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_template import DeviceManagementTemplate
from iograph_models.beta.device_management_template_collection_response import DeviceManagementTemplateCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class TemplatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/templates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementTemplateCollectionResponse:
		"""
		Get templates from deviceManagement
		The available templates
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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementTemplate:
		"""
		Create new navigation property to templates for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementTemplate']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TemplatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TemplatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TemplatesRequest(self.request_adapter, self.path_parameters)

	def by_device_management_template_id(self,
		deviceManagementTemplate_id: str,
	) -> ByDeviceManagementTemplateIdRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id

		from .by_device_management_template_id import ByDeviceManagementTemplateIdRequest
		return ByDeviceManagementTemplateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def import_office365_device_configuration_policies(self,
	) -> ImportOffice365DeviceConfigurationPoliciesRequest:
		from .import_office365_device_configuration_policies import ImportOffice365DeviceConfigurationPoliciesRequest
		return ImportOffice365DeviceConfigurationPoliciesRequest(self.request_adapter, self.path_parameters)

