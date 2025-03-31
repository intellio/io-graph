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
	from .import_office365_device_configuration_policies import ImportOffice365DeviceConfigurationPoliciesRequest
	from .count import CountRequest
	from .by_device_management_template_id1 import ByDeviceManagementTemplateId1Request
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_template_collection_response import DeviceManagementTemplateCollectionResponse
from iograph_models.beta.device_management_template import DeviceManagementTemplate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MigratableToRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/templates/{deviceManagementTemplate%2Did}/migratableTo", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementTemplateCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, DeviceManagementTemplateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementTemplate:
		"""
		Create new navigation property to migratableTo for deviceManagement
		
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


	def with_url(self, raw_url: str) -> MigratableToRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MigratableToRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MigratableToRequest(self.request_adapter, self.path_parameters)

	def by_device_management_template_id1(self,
		deviceManagementTemplate_id: str,
		deviceManagementTemplate_id1: str,
	) -> ByDeviceManagementTemplateId1Request:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")
		if deviceManagementTemplate_id1 is None:
			raise TypeError("deviceManagementTemplate_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id
		path_parameters["deviceManagementTemplate%2Did1"] =  deviceManagementTemplate_id1

		from .by_device_management_template_id1 import ByDeviceManagementTemplateId1Request
		return ByDeviceManagementTemplateId1Request(self.request_adapter, path_parameters)

	def count(self,
		deviceManagementTemplate_id: str,
	) -> CountRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def import_office365_device_configuration_policies(self,
		deviceManagementTemplate_id: str,
	) -> ImportOffice365DeviceConfigurationPoliciesRequest:
		if deviceManagementTemplate_id is None:
			raise TypeError("deviceManagementTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementTemplate%2Did"] =  deviceManagementTemplate_id

		from .import_office365_device_configuration_policies import ImportOffice365DeviceConfigurationPoliciesRequest
		return ImportOffice365DeviceConfigurationPoliciesRequest(self.request_adapter, path_parameters)

