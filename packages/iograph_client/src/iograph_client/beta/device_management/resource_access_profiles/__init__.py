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
	from .query_by_platform_type import QueryByPlatformTypeRequest
	from .count import CountRequest
	from .by_device_management_resource_access_profile_base_id import ByDeviceManagementResourceAccessProfileBaseIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_resource_access_profile_base_collection_response import DeviceManagementResourceAccessProfileBaseCollectionResponse
from iograph_models.beta.device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ResourceAccessProfilesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/resourceAccessProfiles", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementResourceAccessProfileBaseCollectionResponse:
		"""
		Get resourceAccessProfiles from deviceManagement
		Collection of resource access settings associated with account.
		"""
		tags = ['deviceManagement.deviceManagementResourceAccessProfileBase']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementResourceAccessProfileBaseCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementResourceAccessProfileBase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementResourceAccessProfileBase:
		"""
		Create new navigation property to resourceAccessProfiles for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementResourceAccessProfileBase']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementResourceAccessProfileBase, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ResourceAccessProfilesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ResourceAccessProfilesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ResourceAccessProfilesRequest(self.request_adapter, self.path_parameters)

	def by_device_management_resource_access_profile_base_id(self,
		deviceManagementResourceAccessProfileBase_id: str,
	) -> ByDeviceManagementResourceAccessProfileBaseIdRequest:
		if deviceManagementResourceAccessProfileBase_id is None:
			raise TypeError("deviceManagementResourceAccessProfileBase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementResourceAccessProfileBase%2Did"] =  deviceManagementResourceAccessProfileBase_id

		from .by_device_management_resource_access_profile_base_id import ByDeviceManagementResourceAccessProfileBaseIdRequest
		return ByDeviceManagementResourceAccessProfileBaseIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def query_by_platform_type(self,
	) -> QueryByPlatformTypeRequest:
		from .query_by_platform_type import QueryByPlatformTypeRequest
		return QueryByPlatformTypeRequest(self.request_adapter, self.path_parameters)

