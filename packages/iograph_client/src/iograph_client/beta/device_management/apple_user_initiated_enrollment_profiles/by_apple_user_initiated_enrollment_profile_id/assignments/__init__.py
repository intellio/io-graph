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
	from .by_apple_enrollment_profile_assignment_id import ByAppleEnrollmentProfileAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.apple_enrollment_profile_assignment_collection_response import AppleEnrollmentProfileAssignmentCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment


class AssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/appleUserInitiatedEnrollmentProfiles/{appleUserInitiatedEnrollmentProfile%2Did}/assignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AppleEnrollmentProfileAssignmentCollectionResponse:
		"""
		Get assignments from deviceManagement
		The list of assignments for this profile.
		"""
		tags = ['deviceManagement.appleUserInitiatedEnrollmentProfile']

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
		return await self.request_adapter.send_async(request_info, AppleEnrollmentProfileAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: AppleEnrollmentProfileAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AppleEnrollmentProfileAssignment:
		"""
		Create new navigation property to assignments for deviceManagement
		
		"""
		tags = ['deviceManagement.appleUserInitiatedEnrollmentProfile']

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
		return await self.request_adapter.send_async(request_info, AppleEnrollmentProfileAssignment, error_mapping)

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

	def by_apple_enrollment_profile_assignment_id(self,
		appleUserInitiatedEnrollmentProfile_id: str,
		appleEnrollmentProfileAssignment_id: str,
	) -> ByAppleEnrollmentProfileAssignmentIdRequest:
		if appleUserInitiatedEnrollmentProfile_id is None:
			raise TypeError("appleUserInitiatedEnrollmentProfile_id cannot be null.")
		if appleEnrollmentProfileAssignment_id is None:
			raise TypeError("appleEnrollmentProfileAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appleUserInitiatedEnrollmentProfile%2Did"] =  appleUserInitiatedEnrollmentProfile_id
		path_parameters["appleEnrollmentProfileAssignment%2Did"] =  appleEnrollmentProfileAssignment_id

		from .by_apple_enrollment_profile_assignment_id import ByAppleEnrollmentProfileAssignmentIdRequest
		return ByAppleEnrollmentProfileAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		appleUserInitiatedEnrollmentProfile_id: str,
	) -> CountRequest:
		if appleUserInitiatedEnrollmentProfile_id is None:
			raise TypeError("appleUserInitiatedEnrollmentProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appleUserInitiatedEnrollmentProfile%2Did"] =  appleUserInitiatedEnrollmentProfile_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

