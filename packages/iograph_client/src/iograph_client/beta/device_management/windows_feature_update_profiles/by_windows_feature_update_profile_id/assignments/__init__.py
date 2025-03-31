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
	from .count import CountRequest
	from .by_windows_feature_update_profile_assignment_id import ByWindowsFeatureUpdateProfileAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_feature_update_profile_assignment_collection_response import WindowsFeatureUpdateProfileAssignmentCollectionResponse
from iograph_models.beta.windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsFeatureUpdateProfiles/{windowsFeatureUpdateProfile%2Did}/assignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsFeatureUpdateProfileAssignmentCollectionResponse:
		"""
		Get assignments from deviceManagement
		The list of group assignments of the profile.
		"""
		tags = ['deviceManagement.windowsFeatureUpdateProfile']

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
		return await self.request_adapter.send_async(request_info, WindowsFeatureUpdateProfileAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: WindowsFeatureUpdateProfileAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsFeatureUpdateProfileAssignment:
		"""
		Create new navigation property to assignments for deviceManagement
		
		"""
		tags = ['deviceManagement.windowsFeatureUpdateProfile']

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
		return await self.request_adapter.send_async(request_info, WindowsFeatureUpdateProfileAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_windows_feature_update_profile_assignment_id(self,
		windowsFeatureUpdateProfile_id: str,
		windowsFeatureUpdateProfileAssignment_id: str,
	) -> ByWindowsFeatureUpdateProfileAssignmentIdRequest:
		if windowsFeatureUpdateProfile_id is None:
			raise TypeError("windowsFeatureUpdateProfile_id cannot be null.")
		if windowsFeatureUpdateProfileAssignment_id is None:
			raise TypeError("windowsFeatureUpdateProfileAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsFeatureUpdateProfile%2Did"] =  windowsFeatureUpdateProfile_id
		path_parameters["windowsFeatureUpdateProfileAssignment%2Did"] =  windowsFeatureUpdateProfileAssignment_id

		from .by_windows_feature_update_profile_assignment_id import ByWindowsFeatureUpdateProfileAssignmentIdRequest
		return ByWindowsFeatureUpdateProfileAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		windowsFeatureUpdateProfile_id: str,
	) -> CountRequest:
		if windowsFeatureUpdateProfile_id is None:
			raise TypeError("windowsFeatureUpdateProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsFeatureUpdateProfile%2Did"] =  windowsFeatureUpdateProfile_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

