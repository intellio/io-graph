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
	from .validate_filter import ValidateFilterRequest
	from .get_state import GetStateRequest
	from .get_platform_supported_properties_with_platform import GetPlatformSupportedPropertiesWithPlatformRequest
	from .enable import EnableRequest
	from .count import CountRequest
	from .by_device_and_app_management_assignment_filter_id import ByDeviceAndAppManagementAssignmentFilterIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
from iograph_models.beta.device_and_app_management_assignment_filter_collection_response import DeviceAndAppManagementAssignmentFilterCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AssignmentFiltersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/assignmentFilters", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceAndAppManagementAssignmentFilterCollectionResponse:
		"""
		Get assignmentFilters from deviceManagement
		The list of assignment filters
		"""
		tags = ['deviceManagement.deviceAndAppManagementAssignmentFilter']

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
		return await self.request_adapter.send_async(request_info, DeviceAndAppManagementAssignmentFilterCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceAndAppManagementAssignmentFilter,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceAndAppManagementAssignmentFilter:
		"""
		Create new navigation property to assignmentFilters for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceAndAppManagementAssignmentFilter']

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
		return await self.request_adapter.send_async(request_info, DeviceAndAppManagementAssignmentFilter, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignmentFiltersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignmentFiltersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignmentFiltersRequest(self.request_adapter, self.path_parameters)

	def by_device_and_app_management_assignment_filter_id(self,
		deviceAndAppManagementAssignmentFilter_id: str,
	) -> ByDeviceAndAppManagementAssignmentFilterIdRequest:
		if deviceAndAppManagementAssignmentFilter_id is None:
			raise TypeError("deviceAndAppManagementAssignmentFilter_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceAndAppManagementAssignmentFilter%2Did"] =  deviceAndAppManagementAssignmentFilter_id

		from .by_device_and_app_management_assignment_filter_id import ByDeviceAndAppManagementAssignmentFilterIdRequest
		return ByDeviceAndAppManagementAssignmentFilterIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def enable(self,
	) -> EnableRequest:
		from .enable import EnableRequest
		return EnableRequest(self.request_adapter, self.path_parameters)

	def get_platform_supported_properties_with_platform(self,
		platform: str,
	) -> GetPlatformSupportedPropertiesWithPlatformRequest:
		if platform is None:
			raise TypeError("platform cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["platform"] =  platform

		from .get_platform_supported_properties_with_platform import GetPlatformSupportedPropertiesWithPlatformRequest
		return GetPlatformSupportedPropertiesWithPlatformRequest(self.request_adapter, path_parameters)

	@property
	def get_state(self,
	) -> GetStateRequest:
		from .get_state import GetStateRequest
		return GetStateRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_filter(self,
	) -> ValidateFilterRequest:
		from .validate_filter import ValidateFilterRequest
		return ValidateFilterRequest(self.request_adapter, self.path_parameters)

