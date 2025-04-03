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
	from .count import CountRequest
	from .by_enrollment_configuration_assignment_id import ByEnrollmentConfigurationAssignmentIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.enrollment_configuration_assignment_collection_response import EnrollmentConfigurationAssignmentCollectionResponse
from iograph_models.beta.enrollment_configuration_assignment import EnrollmentConfigurationAssignment


class AssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/deviceEnrollmentConfigurations/{deviceEnrollmentConfiguration%2Did}/assignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EnrollmentConfigurationAssignmentCollectionResponse:
		"""
		Get assignments from users
		The list of group assignments for the device configuration profile
		"""
		tags = ['users.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, EnrollmentConfigurationAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: EnrollmentConfigurationAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EnrollmentConfigurationAssignment:
		"""
		Create new navigation property to assignments for users
		
		"""
		tags = ['users.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, EnrollmentConfigurationAssignment, error_mapping)

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

	def by_enrollment_configuration_assignment_id(self,
		user_id: str,
		deviceEnrollmentConfiguration_id: str,
		enrollmentConfigurationAssignment_id: str,
	) -> ByEnrollmentConfigurationAssignmentIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if deviceEnrollmentConfiguration_id is None:
			raise TypeError("deviceEnrollmentConfiguration_id cannot be null.")
		if enrollmentConfigurationAssignment_id is None:
			raise TypeError("enrollmentConfigurationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["deviceEnrollmentConfiguration%2Did"] =  deviceEnrollmentConfiguration_id
		path_parameters["enrollmentConfigurationAssignment%2Did"] =  enrollmentConfigurationAssignment_id

		from .by_enrollment_configuration_assignment_id import ByEnrollmentConfigurationAssignmentIdRequest
		return ByEnrollmentConfigurationAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		deviceEnrollmentConfiguration_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if deviceEnrollmentConfiguration_id is None:
			raise TypeError("deviceEnrollmentConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["deviceEnrollmentConfiguration%2Did"] =  deviceEnrollmentConfiguration_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

